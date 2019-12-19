<template>
    <div class="wrapper">
        <Header />
        <Sidebar />
        <div class="main-panel">
            <div class="content">
                <div class="page-inner">
                    <div class="row">
                        <div class="col-md-12">
                            <button
                            type="button"
                            class="btn"
                            @click="showModal"
                            >
                            Open Modal!
                            </button>
                        </div>
                    </div>
                </div>
            </div>
	    </div>
	</div>
</template>
<script>
    import Header from './Header';
    import Sidebar from './Sidebar';
    export default {
        name: 'pagina2',
        components: {
            Header,
            Sidebar,
        },
        data(){
            return {
                modalVisible: false,
            }
        },
        methods: {
            showModal(){
                this.modalVisible = true;
            },
            closeModal(){
                this.modalVisible = false;
            }
        }
    }
</script>