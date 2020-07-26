<template>
  <v-app id="inspire">
    
    <v-content>
      <D3BarChart :config="config" :datum="data"></D3BarChart>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="start"
          justify="start"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <v-card class="pa-2"
            outlined
            tile>
              <v-toolbar
                color="blue"
                dark
                flat
              >
                <v-toolbar-title>Форма авторизации</v-toolbar-title>
                <v-spacer />
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Логин"
                    name="login"
                    prepend-icon="person"
                    type="text"
                  />

                  <v-text-field
                    id="password"
                    label="Пароль"
                    name="password"
                    prepend-icon="lock"
                    type="password"
                  />
                  
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn color="blue " dark block = True>Войти</v-btn>
                
              </v-card-actions>
              <v-card-actions>
                <v-spacer />
                <v-btn color="blue" dark block = True>Регистарция</v-btn>
                
              </v-card-actions>
              
            </v-card>
            
            
          </v-col>
          <v-col>
          <div>
         
  <p>В состав комплекса CLASS.NET входит:</p>
	<div class="box">
		<ul>
			<li> блоки задач:
				<ul>
          
					<li> тестирующие,</li>
					<li> самообучающие,</li>
					<li> контролирующие;</li>
				</ul>
			</li>
			<li> раздел статистики решения задач;</li>
			<li> раздел статистики по факультету и система рейтингов;</li>
			<li>для преподавателей:
				<ul>
					<li> возможности администрирования группы,</li>
					<li> просмотр статистики решения задач по группе.</li>
				</ul>
        
         <v-data-table
    :headers="headers"
    :items="desserts"
    class="elevation-1"
  >
    <template v-slot:item.calories="{ item }">
      <v-chip :color="getColor(item.calories)" dark>{{ item.calories }}</v-chip>
    </template>
    <template v-slot:item.fat="{ item }">
      <v-chip :color="getColor2(item.fat)" dark>{{ item.fat }}</v-chip>
    </template>
  </v-data-table>
			</li>
		</ul>
	</div>
  </div>
        </v-col>
        </v-row>
      </v-container>
    </v-content>



    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Главная страница</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-format-list-text</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Теория</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-pencil</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Практика</v-list-item-title>
          </v-list-item-content>
        </v-list-item>



      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="blue"
      dark
    >
    
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Меню</v-toolbar-title>
      
    </v-app-bar>

    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          
        </v-row>
      </v-container>
    </v-content>
    <v-footer
      color="blue"
      app
    >
      <span class="white--text">&copy; 2020, Московский Авиационный Институт</span>
    </v-footer>
  </v-app>
</template>

<script>
// data


   export default {
    data () {
      return {
        data : [{
          name: "Lorem",
          total: 30
        },{
          name: "Ipsum",
          total: 21
        },{
          name: "Dolor",
          total: 20
        }],

        // Configuration
        config : [{
          key: "name",
          value: "total",
          color: "steelblue",
        }],
        headers: [
          {
            text: 'Сервисы',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Время(мс)', value: 'calories' },
          { text: 'Статус сервиса', value: 'fat' },
        ],
        desserts: [
          {
            name: 'Пользователи',
            calories: 15,
            fat: 'Ok',
            carbs: 24,
            protein: 4.0,
            iron: '1%',
          },
          {
            name: 'Студенты',
            calories: 10,
            fat: 'Ok',
            carbs: 37,
            protein: 4.3,
            iron: '1%',
          },
          {
            name: 'Теория',
            calories: 7,
            fat: 'Ok',
            carbs: 23,
            protein: 6.0,
            iron: '7%',
          },
          {
            name: 'Практика',
            calories: '60',
            fat: 'Ok',
            carbs: 67,
            protein: 4.3,
            iron: '8%',
          },
        ],
      }
    },
    methods: {
      getColor (calories) {
        if (calories > 400) return 'red'
        else if (calories > 50) return 'orange'
        else return 'green'
      },
      getColor2 (calories) {
        if (calories == 'Ok') return 'green'
      },
    },
  }
</script>