<template>
    <div class="sidebar sidebar-style-2">
        <div class="sidebar-wrapper scrollbar scrollbar-inner">
            <div class="sidebar-content">
                <ul class="nav nav-primary">
                    <li class="nav-item" :class="[currentPage == '/' ? 'active' : '']">
                        <router-link to="/">
                            <i class="fas fa-home"></i>
                            <p>Início</p>
                        </router-link>
                    </li>
                    <li class="nav-item" :class="[currentPage.includes('/pagina2') ? 'active' : '']">
                        <router-link to="/pagina2">
                            <i class="fas fa-home"></i>
                            <p>Pagina 2</p>
                        </router-link>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Sidebar',
        data() {
            return{

            }
        },
        computed: {
            currentPage(){
                console.log(this.$route.path);
                return this.$route.path;
            },
        },
    }
</script>