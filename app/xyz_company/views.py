from django.shortcuts import render , redirect , get_object_or_404
from core.models import Portfolio, Services, CompanyHistory , Team
from django.http import JsonResponse
from django.contrib import messages
 


def Home(request):
    """this function render the home template"""
    portfolio_list =  Portfolio.objects.all()
    services_list = Services.objects.all()
    company_history = CompanyHistory.objects.all()
    team_list = Team.objects.all()
    context = {
                "title":"home",
                "portfolio_list":portfolio_list,
                "services_list":services_list,
                "company_history":company_history,
                "team_list":team_list,
            }
    return render(request, 'xyz_company/home.html', context)




def dump_testing_data(request):
    """this function is used to populate our model -testing  """
    portfolio_list =   [{
                    "name":"Threads",
                    "description":"Illustration",
                 
                    "img_url":"/img/portfolio/1.jpg",
                    "id":1,
                    },{
                    "name":"Explore",
                    "description":"Graphic Design",                   
                     "img_url":"/img/portfolio/2.jpg",
                     "id":2,
                    },
                    {
                    "name":"Finish",
                    "description":"Identity",                  
                     "img_url":"/img/portfolio/3.jpg",
                      "id":3,
                    },
                    {
                    "name":"Lines",
                    "description":"Branding",                   
                     "img_url":"/img/portfolio/4.jpg",
                      "id":4,
                    }, {
                    "name":"Southwest",
                    "description":"Website Design",                   
                     "img_url":"/img/portfolio/5.jpg",
                     "id":5,
                    },
                     {
                    "name":"Window",
                    "description":"Photography",
                     "img_url":"/img/portfolio/6.jpg",
                     "id":6,
                    },
                  
                  
                ]


    # for item in portfolio_list:
    #     entry = Portfolio(name=item['name'],
    #                         description=item['description'],
    #                         img_url=item['img_url'],
    #                  )
    #     entry.save()


    services_list =   [{
                    "product_name":"E-Commerce",
                    "product_description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima maxime quam architecto quo inventore harum ex magni, dicta impedit.",
                    
                     "class_name":"fas fa-shopping-cart fa-stack-1x fa-inverse",
                     "id":1,
                    },
                    {
                    "product_name":"Responsive Design",
                    "product_description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima maxime quam architecto quo inventore harum ex magni, dicta impedit.",
                    "class_name":"fas fa-laptop fa-stack-1x fa-inverse",
                    "id":2, 
                    },
                    {
                    "product_name":"Web Security",
                    "product_description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima maxime quam architecto quo inventore harum ex magni, dicta impedit.",
                     "class_name":"fas fa-lock fa-stack-1x fa-inverse",
                     "id":3,
                    },
                ]


    # for item in services_list:
    #     entry = Services(name=item['product_name'],
    #                         description=item['product_name'],
    #                         css_class=item['class_name'],
    #                  )
    #     entry.save()


    
    company_history =  [{
                    "name":" Humble Beginnings",
                    "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente, totam reiciendis temporibus qui quibusdam, recusandae sit vero unde, sed, incidunt et ea quo dolore laudantium consectetur!",
                    "img_url":"/img/about/1.jpg",
                    "date":"2009-2011",
                    "id":1,
                   
                    }, {
                    "name":"An Agency is Born",
                    "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente, totam reiciendis temporibus qui quibusdam, recusandae sit vero unde, sed, incidunt et ea quo dolore laudantium consectetur!",
                    "img_url":"/img/about/2.jpg",
                    "date":"March 2011",
                    "id":2,
                   
                    },{
                    "name":"Transition to Full Service",
                    "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente, totam reiciendis temporibus qui quibusdam, recusandae sit vero unde, sed, incidunt et ea quo dolore laudantium consectetur!",
                    "img_url":"/img/about/3.jpg",
                    "date":"December 2015",
                    "id":3,
                   
                    },{
                    "name":"Phase Two Expansion",
                    "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente, totam reiciendis temporibus qui quibusdam, recusandae sit vero unde, sed, incidunt et ea quo dolore laudantium consectetur!",
                    "img_url":"/img/about/4.jpg",
                    "date":"July 2020",
                    "id":4,
                   
                    }, 
                    
                ]

    # for item in company_history:
    #     entry = CompanyHistory(name=item['name'],
    #                         description=item['description'],
    #                         date=item['date'],
    #                         img_url=item['img_url'],
    #                  )
    #     entry.save()
    team_list =  [{
                    "name":"Parveen Anand",
                    "title":"Lead Designer",
                    "img_url":"/img/team/1.jpg",
                    "id":1,
                   
                    },{
                    "name":"Diana Petersen",
                    "title":"Lead Marketer",
                      "img_url":"/img/team/2.jpg",
                    "id":2,
                   
                    },
                    {
                    "name":"Larry Parker",
                    "title":"Lead Developer",
                    "img_url":"/img/team/3.jpg",
                    "id":3,
                     
                    },
                    
                ]

    for item in team_list:
        entry = Team(name=item['name'],
                     title=item['title'],
                    img_url=item['img_url'],
                     )
        entry.save()
 
    return  JsonResponse({"result":"check db"}, status=200)


