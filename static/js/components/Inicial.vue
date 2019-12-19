<template>
    <div class="inicial">
        <Header/>
        <div class="container custom-container p-0">
            <div class="row">
                <div class="col-md-12">
                    <div class="mt-20"></div>
                    You chose {{ $store.getters.pessoa.cpf }}
                    <Passo1 v-if="passo==1" @mudarPasso="mudarPasso" v-model="pessoa"/>
                    <Passo2 v-else-if="passo==2" @pageSuccess="pageSuccess"/>
                    <Passo3 v-else-if="passo==3" :resultado="resultado"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Header from './Header';
    import Sidebar from './Sidebar';
    import { api } from '../api/http-common';
    import Swal from 'sweetalert2';
    import Passo1 from './Forms/Passo1'
    import Passo2 from './Forms/Passo2'
    import Passo3 from './Forms/Passo3'


    export default {
        name: 'inicial',
        components: {
            Header,
            Sidebar,
            Passo1,
            Passo2,
            Passo3,
        },
        methods: {
            mudarPasso(val){
                this.passo = val;
            },
            pageSuccess(val){
                this.resultado = val;
                this.passo = 3;
            }
        },
        data() {
            return{
                title: document.title,
                passo: 1,
                resultado: null,
                pessoa: {},
            }
        },
        watch: {
            passo: function(){
                document.title = this.title + ' - Passo ' + this.passo;
            },
            'pessoa.cpf': function(){
                console.log(this.pessoa);
            },
        },
        mounted() {
            api.get(`status/`)
            .then(res => {
                console.log(res.data);
            });
        },
        created(){
            let title = document.title;
            document.title = this.title + ' - Passo ' + this.passo;
        }
    }
</script>

<style>
    .custom-container{
        max-width: 750px;   
    }
    .mt-20{
        margin-top: 4rem;
    }
</style>