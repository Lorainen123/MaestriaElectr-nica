import Node611


#Fuzzy Controller 

Vrefd = ctrl.Consequent(np.arange(-2, 2, 0.1), 'Vrefd')
Pdif = ctrl.Antecedent(np.arange(-200, 200, 0.01),'Pdif')

#Membership functions

#Pdif

Pdif['N'] = fuzz.trampf(Pdif.universe, [-100,-2, -0.2, -0.01])
Pdif['P'] = fuzz.trampf(Pdif.universe, [0.01, 0.2, 2, 100])
Pdif['Z'] = fuzz.trimf(Pdif.universe, [-0.01,0,0.01])


#Vref

Vrefd['N'] = fuzz.trimf(Vrefd.universe, [-0.2, -0.1, 0])
Vrefd['P'] = fuzz.trimf(Vrefd.universe, [0, 0.1, 0.2])
Vrefd['Z'] = fuzz.trimf(Vrefd.universe, [-0.01, 0, 0.01])

##Rules

rule1=ctrl.Rule(Pdif['P'],Vrefd['P'])
rule2=ctrl.Rule(Pdif['N'],Vrefd['N'])
rule3=ctrl.Rule(Pdif['Z'],Vrefd['Z'])

vref_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
vrefout = ctrl.ControlSystemSimulation(vref_ctrl)

vrefout.input['Pdif']=0.1
vrefout.compute()
Vrefin=round(vrefout.output['Vrefd'],2)
