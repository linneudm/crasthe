<template>
	<div class="formulario-passo1">

	  <div class="form-row">
	    <div class="form-group col-md-6">
	      <label for="cpf">CPF</label>
	      <input type="text" class="form-control" id="cpf" placeholder="CPF" v-model="pessoa.cpf">
	    </div>
	    <div class="form-group col-md-6">
	      <label for="data-nascimento">Data de Nascimento</label>
	      <input type="text" class="form-control" id="data-nascimento" placeholder="Data de Nascimento">
	    </div>
	  </div>
	  <div class="form-row">
	    <div class="form-group col-md-12">
	      <label for="nome">Nome</label>
	      <input type="text" class="form-control" id="nome" placeholder="Nome">
	    </div>
	  </div>
	  <div class="form-row">
	    <div class="form-group col-md-12">
	      <label for="email">Email</label>
	      <input type="email" class="form-control" id="email" placeholder="Email">
	    </div>
	  </div>
	  <div class="form-row">
	    <div class="form-group col-md-2">
	      <label for="ddd-fone">DDD</label>
	      <input type="text" class="form-control" id="ddd-fone" placeholder="DDD" v-mask="'(##)'">
	    </div>
	    <div class="form-group col-md-4">
	      <label for="fone">Telefone</label>
	      <input type="text" class="form-control" id="fone" placeholder="Telefone">
	    </div>
	    <div class="form-group col-md-2">
	      <label for="ddd-celular">DDD</label>
	      <input type="text" class="form-control" id="ddd-celular" placeholder="DDD">
	    </div>
	    <div class="form-group col-md-4">
	      <label for="celular">Celular</label>
	      <input type="text" class="form-control" id="celular" placeholder="Celular">
	    </div>
	  </div>
	  <button type="submit" class="btn btn-primary" @click="handleMudanca()">Entrar</button>
	  <button type="submit" class="btn btn-primary" @click="enviaPessoa">Enviar</button>
	</div>
</template>

<script>
	import Modal from '../Modal';
	import Swal from 'sweetalert2';
    export default {
        name: 'passo1',
        components: { Modal },
        mounted() {},
        data(){
        	return {
        		modal: true,
        		pessoa: {
        			cpf: null,
        		},
        	}
        },
        methods: {
            checkAgenda(){
	            return true;
            },
        	handleMudanca(){
        		this.enviaPessoa();
        		let ok = this.checkAgenda();
        		if(ok){
        			this.$emit('mudarPasso', 2);
        		}else{
        			this.enviaPessoa(true);
		            let msgmodal = `
		                Não é possivel efetuar um novo agendamento.
		                Existe o protocolo de agendamento número 940640 no local CRAS SE para o
		                dia 23/01/2020 as 12:30hs.<br/><br/>

		                Opções:<br/>
		                1-Efetuar um reagendamento para esse protocolo. Para isso acesse a aba "Consultar
		                Agendamento."<br/>
		                2-Cancelar o agendamento para esse protocolo. Para isso acesse a aba "Consultar
		                Agendamento."<br/>
		                3-Aguardar a referida data e horário para comparecer ao local e realizar seu atendimento.<br/>
		            `;
		            Swal.fire({
		              title:'Atenção',
		              html: msgmodal,
		              icon: 'error',
		              confirmButtonText: 'Fechar.'
		            })
        		}
        	},
        	enviaPessoa(){
        		this.$store.commit('change', this.pessoa);
        	},
        },
        created(){
        	let city = "<b>Teresina</b>";
        	let msgmodal = `
				Este agendamento destina-se apenas para as famílias residentes na cidade de ${city}.
				Se sua família reside em outra cidade, procure a Prefeitura de seu Município.
        	`;
			Swal.fire({
			  title:'Atenção',
			  html: msgmodal,
			  icon: 'info',
			  confirmButtonText: 'Ok, entendi.'
			})
        },
    }
</script>

<style>

</style>