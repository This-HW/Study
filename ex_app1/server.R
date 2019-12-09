library(shiny)
shinyServer(function(input, output){
  sliderValues <- reactive({
    data.frame(
      Parameter="BBB",
      Value = as.character(input$aaa)
    ) 
    
  })
  output$values <- renderTable({
    sliderValues()
  })
  # output$values <- renderPrint({
  #  sliderValues()
  # })
})