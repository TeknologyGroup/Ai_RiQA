describe('Simulation Page', () => {
  it('should run a simulation successfully', () => {
    cy.visit('/simulate')
    
    cy.get('select').select('wormhole')
    cy.get('textarea').type('{"mass": 10, "charge": 5}')
    
    cy.intercept('POST', 'http://localhost:5000/api/simulate', {
      statusCode: 200,
      body: { result: "success" }
    }).as('simulationRequest')
    
    cy.get('button').contains('Start Simulation').click()
    cy.wait('@simulationRequest')
    
    cy.contains('Results').should('be.visible')
  })
})
