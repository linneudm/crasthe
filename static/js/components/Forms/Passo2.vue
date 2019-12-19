<template>
	<div class="formulario-passo2">
		Passo2
        Horarios:
        <button v-for="(h,key) in horarios" class="btn btn-primary" :class="{'btn-success': active == key}" @click="active = key">{{h}}</button>
	   <button type="submit" class="btn btn-primary" @click="handleMudanca()">Entrar</button>
	</div>
</template>

<script>
    import Swal from 'sweetalert2';
    import { api } from '../../api/http-common';
    export default {
        name: 'passo2',
        data() {
            return {
                horarios: [],
                active: null,
            }
        },
        created(){
            api.get(`/agenda/get_horarios/`)
            .then(res => {
                console.log(res.data.horarios);
                this.horarios = res.data.horarios;
            });
        },
        mounted(){},
        methods: {
        	handleMudanca(){
        		let ok = true;
        		if(ok){
        			this.$emit('pageSuccess', 'deu mto bom po!');
        		}
        	}
        },
    }
</script>

<style>

</style>