'''
 This file is part of PyCoTools.

 PyCoTools is free software: you can redistribute it and/or modify
 it under the terms of the GNU Lesser General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 PyCoTools is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public License
 along with PyCoTools.  If not, see <http://www.gnu.org/licenses/>.


Author: 
    Ciaran Welsh
Date:
    12/03/2017

 Object:
 
'''
import unittest
import os
import re
import pandas
import numpy
import scipy
import PyCoTools
import glob
import shutil





model_string='''<?xml version="1.0" encoding="UTF-8"?>
<!-- generated with COPASI 4.16 (Build 104) (http://www.copasi.org) at 2016-10-27 14:41:02 UTC -->
<?oxygen RNGSchema="http://www.copasi.org/static/schema/CopasiML.rng" type="xml"?>
<COPASI xmlns="http://www.copasi.org/static/schema" versionMajor="4" versionMinor="16" versionDevel="104" copasiSourcesModified="0">
  <ListOfFunctions>
    <Function key="Function_40" name="Function for Ligand receptor complex formation" type="UserDefined" reversible="false">
      <Expression>
        ka*ligand*(RI*PM)*(RII*PM)/PM
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_266" name="PM" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_258" name="RI" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_268" name="RII" order="2" role="substrate"/>
        <ParameterDescription key="FunctionParameter_264" name="ka" order="3" role="constant"/>
        <ParameterDescription key="FunctionParameter_254" name="ligand" order="4" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_41" name="Function for Ligand receptor complex constitutive degradation" type="UserDefined" reversible="false">
      <Expression>
        kcd*(lRIRII*PM)/PM
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_262" name="PM" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_269" name="kcd" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_265" name="lRIRII" order="2" role="substrate"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_42" name="Function for Ligand independent complex degradation" type="UserDefined" reversible="false">
      <Expression>
        klid*(lRIRII*PM)/PM
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_272" name="PM" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_270" name="klid" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_267" name="lRIRII" order="2" role="substrate"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_43" name="Function for Ligand receptor complex internalization" type="UserDefined" reversible="false">
      <Expression>
        ki*(lRIRII*PM)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_275" name="PM" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_273" name="ki" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_246" name="lRIRII" order="2" role="substrate"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_44" name="Function for RI synthesis" type="UserDefined" reversible="false">
      <Expression>
        pRI/PM
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_271" name="PM" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_276" name="pRI" order="1" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_45" name="Function for RI constitutive degradation" type="UserDefined" reversible="false">
      <Expression>
        kcd*(RI*PM)/PM
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_280" name="PM" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_278" name="RI" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_277" name="kcd" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_46" name="Function for RI internalization" type="UserDefined" reversible="false">
      <Expression>
        ki*(RI*PM)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_283" name="PM" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_274" name="RI" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_281" name="ki" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_47" name="Function for RI recycling" type="UserDefined" reversible="false">
      <Expression>
        kr*(RI_endo*Endosome)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_286" name="Endosome" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_279" name="RI_endo" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_284" name="kr" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_48" name="Function for Ligand Receptor complex recycling" type="UserDefined" reversible="false">
      <Expression>
        kr*(lRIRII_endo*Endosome)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_289" name="Endosome" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_287" name="kr" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_282" name="lRIRII_endo" order="2" role="substrate"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_49" name="Function for RII synthesis" type="UserDefined" reversible="false">
      <Expression>
        pRII/PM
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_285" name="PM" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_290" name="pRII" order="1" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_50" name="Function for RII constitutive degradation" type="UserDefined" reversible="false">
      <Expression>
        kcd*(RII*PM)/PM
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_294" name="PM" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_292" name="RII" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_291" name="kcd" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_51" name="Function for RII internalization" type="UserDefined" reversible="false">
      <Expression>
        ki*(RII*PM)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_297" name="PM" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_288" name="RII" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_295" name="ki" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_52" name="Function for RII recycling" type="UserDefined" reversible="false">
      <Expression>
        kr*(RII_endo*Endosome)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_300" name="Endosome" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_293" name="RII_endo" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_298" name="kr" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
  </ListOfFunctions>
  <model key="model_3" name="Vilar2006_TGFbeta" simulationType="time" timeUnit="h" volumeUnit="l" areaUnit="m²" lengthUnit="m" quantityUnit="#" type="stochastic" avogadroConstant="6.02214179e+023">
    <MiriamAnnotation>
<rdf:Rdf
   xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#"
   xmlns:dcterms="http://purl.org/dc/terms/"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <rdf:Description rdf:about="#model_3">
    <dcterms:bibliographicCitation>
      <rdf:Bag>
        <rdf:li>
          <rdf:Description>
            <CopasiMT:isDescribedBy rdf:resource="http://identifiers.org/pubmed/16446785"/>
          </rdf:Description>
        </rdf:li>
      </rdf:Bag>
    </dcterms:bibliographicCitation>
    <dcterms:created>
      <rdf:Description>
        <dcterms:W3CDTF>2006-11-28T18:39:38Z</dcterms:W3CDTF>
      </rdf:Description>
    </dcterms:created>
    <dcterms:creator>
      <rdf:Bag>
        <rdf:li>
          <rdf:Description>
            <vCard:EMAIL>hdharuri@cds.caltech.edu</vCard:EMAIL>
            <vCard:N>
              <rdf:Description>
                <vCard:Family>Dharuri</vCard:Family>
                <vCard:Given>Harish</vCard:Given>
              </rdf:Description>
            </vCard:N>
            <vCard:ORG>
              <rdf:Description>
                <vCard:Orgname>California Institute of Technology</vCard:Orgname>
              </rdf:Description>
            </vCard:ORG>
          </rdf:Description>
        </rdf:li>
      </rdf:Bag>
    </dcterms:creator>
    <dcterms:modified>
      <rdf:Description>
        <dcterms:W3CDTF>2012-07-05T14:45:52Z</dcterms:W3CDTF>
      </rdf:Description>
    </dcterms:modified>
    <CopasiMT:hasPart>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_6844.3"/>
      </rdf:Bag>
    </CopasiMT:hasPart>
    <CopasiMT:hasPart>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/kegg.pathway/hsa04350"/>
      </rdf:Bag>
    </CopasiMT:hasPart>
    <CopasiMT:is>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/biomodels.db/MODEL4023382414"/>
      </rdf:Bag>
    </CopasiMT:is>
    <CopasiMT:is>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/biomodels.db/BIOMD0000000101"/>
      </rdf:Bag>
    </CopasiMT:is>
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0007179"/>
      </rdf:Bag>
    </CopasiMT:isVersionOf>
    <CopasiMT:occursIn>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/taxonomy/131567"/>
      </rdf:Bag>
    </CopasiMT:occursIn>
  </rdf:Description>
</rdf:Rdf>

    </MiriamAnnotation>
    <Comment>
      <body xmlns="http://www.w3.org/1999/xhtml">
    <p>The model reproduces Fig 5A of the paper. The ligand concentration is increased from 3E-5 to 0.01 at time t=2500 to ensure that the system  reaches steady state. Hence, the time t=0 of the paper corresponds to t=2500 in the model. The peak value of the active ligand receptor complex is off by a value of 1.25, the authors have stated that this discrepancy is due to the fact that the figure in the paper corresponds to a slightly different parameter set. The model was successfully tested on MathSBML.</p>
    <br />
    <p>To the extent possible under law, all copyright and related or neighbouring rights to this encoded model have been dedicated to the public domain worldwide. Please refer to      <a href="http://creativecommons.org/publicdomain/zero/1.0/" title="Creative Commons CC0">CC0 Public Domain Dedication</a>
          for more information.      </p>
  <p>In summary, you are entitled to use this encoded model in absolutely any manner you deem suitable, verbatim, or with modification, alone or embedded it in a larger context, redistribute it, commercially or not, in a restricted way or not.</p>
  <br />
  <p>To cite Biomodels Database, please use:      <a href="http://www.ncbi.nlm.nih.gov/pubmed/20587024" target="_blank">Li C, Donizelli M, Rodriguez N, Dharuri H, Endler L, Chelliah V, Li L, He E, Henry A, Stefan MI, Snoep JL, Hucka M, Le Novère N, Laibe C (2010) Biomodels Database: An enhanced, curated and annotated resource for published quantitative kinetic models. BMC Syst Biol., 4:92.</a>
</p>
</body>
    </Comment>
    <ListOfCompartments>
      <Compartment key="Compartment_1" name="Plasma membrane" simulationType="fixed" dimensionality="3">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Compartment_1">
    <CopasiMT:is>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0005886" />
      </rdf:Bag>
    </CopasiMT:is>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
      </Compartment>
      <Compartment key="Compartment_3" name="Endosome" simulationType="fixed" dimensionality="3">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Compartment_3">
    <CopasiMT:is>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0005768" />
      </rdf:Bag>
    </CopasiMT:is>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
      </Compartment>
    </ListOfCompartments>
    <ListOfmetabolites>
      <Metabolite key="Metabolite_1" name="Receptor 1" simulationType="reactions" compartment="Compartment_1">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Metabolite_1">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/uniprot/P36897" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_3" name="Receptor 2" simulationType="reactions" compartment="Compartment_1">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Metabolite_3">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/uniprot/P37173" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_5" name="ligand receptor complex-plasma membrane" simulationType="reactions" compartment="Compartment_1">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Metabolite_5">
    <CopasiMT:hasPart>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/uniprot/P01137" />
        <rdf:li rdf:resource="http://identifiers.org/uniprot/P36897" />
        <rdf:li rdf:resource="http://identifiers.org/uniprot/P37173" />
      </rdf:Bag>
    </CopasiMT:hasPart>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_7" name="ligand receptor complex-endosome" simulationType="reactions" compartment="Compartment_3">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Metabolite_7">
    <CopasiMT:hasPart>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/uniprot/P01137" />
        <rdf:li rdf:resource="http://identifiers.org/uniprot/P36897" />
        <rdf:li rdf:resource="http://identifiers.org/uniprot/P37173" />
      </rdf:Bag>
    </CopasiMT:hasPart>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_9" name="Receptor 1-endosome" simulationType="reactions" compartment="Compartment_3">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Metabolite_9">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/uniprot/P36897" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_11" name="Receptor 2 endosome" simulationType="reactions" compartment="Compartment_3">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Metabolite_11">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/uniprot/P37173" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
      </Metabolite>
    </ListOfmetabolites>
    <ListOfmodelValues>
      <modelValue key="modelValue_0" name="ka" simulationType="fixed">
      </modelValue>
      <modelValue key="modelValue_1" name="ligand" simulationType="fixed">
      </modelValue>
      <modelValue key="modelValue_2" name="kcd" simulationType="fixed">
      </modelValue>
      <modelValue key="modelValue_3" name="klid" simulationType="fixed">
      </modelValue>
      <modelValue key="modelValue_4" name="ki" simulationType="fixed">
      </modelValue>
      <modelValue key="modelValue_5" name="pRI" simulationType="fixed">
      </modelValue>
      <modelValue key="modelValue_6" name="kr" simulationType="fixed">
      </modelValue>
      <modelValue key="modelValue_7" name="alpha" simulationType="fixed">
      </modelValue>
      <modelValue key="modelValue_8" name="pRII" simulationType="fixed">
      </modelValue>
    </ListOfmodelValues>
    <ListOfReactions>
      <Reaction key="Reaction_0" name="Ligand receptor complex formation" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_0">
    <CopasiMT:is>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0007181" />
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0050431" />
      </rdf:Bag>
    </CopasiMT:is>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_3" stoichiometry="1"/>
          <Substrate metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_5" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4396" name="ka" value="0.779862"/>
          <Constant key="Parameter_4395" name="ligand" value="0.0001"/>
        </ListOfConstants>
        <KineticLaw function="Function_40">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_266">
              <SourceParameter reference="Compartment_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_258">
              <SourceParameter reference="Metabolite_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_268">
              <SourceParameter reference="Metabolite_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_264">
              <SourceParameter reference="modelValue_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_254">
              <SourceParameter reference="modelValue_1"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_1" name="Ligand receptor complex constitutive degradation" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_1">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0030512" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_5" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_4394" name="kcd" value="0.0251133"/>
        </ListOfConstants>
        <KineticLaw function="Function_41">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_262">
              <SourceParameter reference="Compartment_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_269">
              <SourceParameter reference="modelValue_2"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_265">
              <SourceParameter reference="Metabolite_5"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_2" name="Ligand independent complex degradation" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_2">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0030512" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_5" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_4393" name="klid" value="0.268159"/>
        </ListOfConstants>
        <KineticLaw function="Function_42">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_272">
              <SourceParameter reference="Compartment_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_270">
              <SourceParameter reference="modelValue_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_267">
              <SourceParameter reference="Metabolite_5"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_3" name="Ligand receptor complex internalization" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_3">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0030511" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_5" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_7" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4392" name="ki" value="0.390589"/>
        </ListOfConstants>
        <KineticLaw function="Function_43">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_275">
              <SourceParameter reference="Compartment_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_273">
              <SourceParameter reference="modelValue_4"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_246">
              <SourceParameter reference="Metabolite_5"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_4" name="RI synthesis" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_4">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0006412" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfProducts>
          <Product metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4391" name="pRI" value="6.44406"/>
        </ListOfConstants>
        <KineticLaw function="Function_44">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_271">
              <SourceParameter reference="Compartment_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_276">
              <SourceParameter reference="modelValue_5"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_5" name="RI constitutive degradation" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_5">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0032801" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_4390" name="kcd" value="0.0251133"/>
        </ListOfConstants>
        <KineticLaw function="Function_45">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_280">
              <SourceParameter reference="Compartment_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_278">
              <SourceParameter reference="Metabolite_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_277">
              <SourceParameter reference="modelValue_2"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_6" name="RI internalization" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_6">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0031623" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_9" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4389" name="ki" value="0.390589"/>
        </ListOfConstants>
        <KineticLaw function="Function_46">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_283">
              <SourceParameter reference="Compartment_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_274">
              <SourceParameter reference="Metabolite_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_281">
              <SourceParameter reference="modelValue_4"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_7" name="RI recycling" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_7">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0001881" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_9" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4388" name="kr" value="0.0308656"/>
        </ListOfConstants>
        <KineticLaw function="Function_47">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_286">
              <SourceParameter reference="Compartment_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_279">
              <SourceParameter reference="Metabolite_9"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_284">
              <SourceParameter reference="modelValue_6"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_8" name="Ligand Receptor complex recycling" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_8">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0001881" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_7" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_1" stoichiometry="1"/>
          <Product metabolite="Metabolite_3" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4387" name="kr" value="0.0308656"/>
        </ListOfConstants>
        <KineticLaw function="Function_48">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_289">
              <SourceParameter reference="Compartment_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_287">
              <SourceParameter reference="modelValue_6"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_282">
              <SourceParameter reference="Metabolite_7"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_9" name="RII synthesis" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_9">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0006412" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfProducts>
          <Product metabolite="Metabolite_3" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4386" name="pRII" value="4.20542"/>
        </ListOfConstants>
        <KineticLaw function="Function_49">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_285">
              <SourceParameter reference="Compartment_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_290">
              <SourceParameter reference="modelValue_8"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_10" name="RII constitutive degradation" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_10">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0032801" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_3" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_4385" name="kcd" value="0.0251133"/>
        </ListOfConstants>
        <KineticLaw function="Function_50">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_294">
              <SourceParameter reference="Compartment_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_292">
              <SourceParameter reference="Metabolite_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_291">
              <SourceParameter reference="modelValue_2"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_11" name="RII internalization" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_11">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0031623" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_3" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4384" name="ki" value="0.390589"/>
        </ListOfConstants>
        <KineticLaw function="Function_51">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_297">
              <SourceParameter reference="Compartment_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_288">
              <SourceParameter reference="Metabolite_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_295">
              <SourceParameter reference="modelValue_4"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_12" name="RII recycling" reversible="false" fast="false">
        <MiriamAnnotation>
<rdf:Rdf xmlns:CopasiMT="http://www.copasi.org/Rdf/MiriamTerms#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Reaction_12">
    <CopasiMT:isVersionOf>
      <rdf:Bag>
        <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0001881" />
      </rdf:Bag>
    </CopasiMT:isVersionOf>
  </rdf:Description>
</rdf:Rdf>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_3" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4383" name="kr" value="0.0308656"/>
        </ListOfConstants>
        <KineticLaw function="Function_52">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_300">
              <SourceParameter reference="Compartment_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_293">
              <SourceParameter reference="Metabolite_11"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_298">
              <SourceParameter reference="modelValue_6"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
    </ListOfReactions>
    <ListOfEvents>
      <Event key="Event_0" name="event_0000001" fireAtInitialTime="0" persistentTrigger="0">
        <TriggerExpression>
          &lt;CN=Root,model=Vilar2006_TGFbeta,Reference=Time&gt; ge 2500
        </TriggerExpression>
        <ListOfAssignments>
          <Assignment targetKey="modelValue_1">
            <Expression>
              0.01
            </Expression>
          </Assignment>
        </ListOfAssignments>
      </Event>
    </ListOfEvents>
    <ListOfmodelParameterSets activeSet="modelParameterSet_1">
      <modelParameterSet key="modelParameterSet_1" name="Initial State">
        <modelParameterGroup cn="String=Initial Time" type="Group">
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta" value="0" type="model" simulationType="time"/>
        </modelParameterGroup>
        <modelParameterGroup cn="String=Initial Compartment Sizes" type="Group">
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Plasma membrane]" value="1" type="Compartment" simulationType="fixed"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Endosome]" value="1" type="Compartment" simulationType="fixed"/>
        </modelParameterGroup>
        <modelParameterGroup cn="String=Initial Species Values" type="Group">
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Plasma membrane],Vector=metabolites[Receptor 1]" value="22.9544" type="Species" simulationType="reactions"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Plasma membrane],Vector=metabolites[Receptor 2]" value="0.00155182" type="Species" simulationType="reactions"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Plasma membrane],Vector=metabolites[ligand receptor complex-plasma membrane]" value="0.0001" type="Species" simulationType="reactions"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Endosome],Vector=metabolites[ligand receptor complex-endosome]" value="38.8192950146758" type="Species" simulationType="reactions"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Endosome],Vector=metabolites[Receptor 1-endosome]" value="7.62219" type="Species" simulationType="reactions"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Endosome],Vector=metabolites[Receptor 2 endosome]" value="0.385859" type="Species" simulationType="reactions"/>
        </modelParameterGroup>
        <modelParameterGroup cn="String=Initial Global Quantities" type="Group">
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ka]" value="0.7798620000000001" type="modelValue" simulationType="fixed"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ligand]" value="0.0001" type="modelValue" simulationType="fixed"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[kcd]" value="0.0251133" type="modelValue" simulationType="fixed"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[klid]" value="0.268159" type="modelValue" simulationType="fixed"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ki]" value="0.390589" type="modelValue" simulationType="fixed"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[pRI]" value="6.44406" type="modelValue" simulationType="fixed"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[kr]" value="0.0308656" type="modelValue" simulationType="fixed"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[alpha]" value="1.04518" type="modelValue" simulationType="fixed"/>
          <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[pRII]" value="4.20542" type="modelValue" simulationType="fixed"/>
        </modelParameterGroup>
        <modelParameterGroup cn="String=Kinetic Parameters" type="Group">
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[Ligand receptor complex formation]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[Ligand receptor complex formation],ParameterGroup=Parameters,Parameter=ka" value="0.7798620000000001" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ka],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[Ligand receptor complex formation],ParameterGroup=Parameters,Parameter=ligand" value="0.0001" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ligand],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[Ligand receptor complex constitutive degradation]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[Ligand receptor complex constitutive degradation],ParameterGroup=Parameters,Parameter=kcd" value="0.0251133" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[kcd],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[Ligand independent complex degradation]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[Ligand independent complex degradation],ParameterGroup=Parameters,Parameter=klid" value="0.268159" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[klid],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[Ligand receptor complex internalization]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[Ligand receptor complex internalization],ParameterGroup=Parameters,Parameter=ki" value="0.390589" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ki],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RI synthesis]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RI synthesis],ParameterGroup=Parameters,Parameter=pRI" value="6.44406" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[pRI],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RI constitutive degradation]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RI constitutive degradation],ParameterGroup=Parameters,Parameter=kcd" value="0.0251133" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[kcd],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RI internalization]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RI internalization],ParameterGroup=Parameters,Parameter=ki" value="0.390589" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ki],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RI recycling]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RI recycling],ParameterGroup=Parameters,Parameter=kr" value="0.0308656" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[kr],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[Ligand Receptor complex recycling]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[Ligand Receptor complex recycling],ParameterGroup=Parameters,Parameter=kr" value="0.0308656" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[kr],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RII synthesis]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RII synthesis],ParameterGroup=Parameters,Parameter=pRII" value="4.20542" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[pRII],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RII constitutive degradation]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RII constitutive degradation],ParameterGroup=Parameters,Parameter=kcd" value="0.0251133" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[kcd],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RII internalization]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RII internalization],ParameterGroup=Parameters,Parameter=ki" value="0.390589" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ki],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
          <modelParameterGroup cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RII recycling]" type="Reaction">
            <modelParameter cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Reactions[RII recycling],ParameterGroup=Parameters,Parameter=kr" value="0.0308656" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,model=Vilar2006_TGFbeta,Vector=Values[kr],Reference=InitialValue&gt;
              </InitialExpression>
            </modelParameter>
          </modelParameterGroup>
        </modelParameterGroup>
      </modelParameterSet>
    </ListOfmodelParameterSets>
    <StateTemplate>
      <StateTemplatevariable objectReference="model_3"/>
      <StateTemplatevariable objectReference="Metabolite_1"/>
      <StateTemplatevariable objectReference="Metabolite_3"/>
      <StateTemplatevariable objectReference="Metabolite_5"/>
      <StateTemplatevariable objectReference="Metabolite_7"/>
      <StateTemplatevariable objectReference="Metabolite_9"/>
      <StateTemplatevariable objectReference="Metabolite_11"/>
      <StateTemplatevariable objectReference="Compartment_1"/>
      <StateTemplatevariable objectReference="Compartment_3"/>
      <StateTemplatevariable objectReference="modelValue_0"/>
      <StateTemplatevariable objectReference="modelValue_1"/>
      <StateTemplatevariable objectReference="modelValue_2"/>
      <StateTemplatevariable objectReference="modelValue_3"/>
      <StateTemplatevariable objectReference="modelValue_4"/>
      <StateTemplatevariable objectReference="modelValue_5"/>
      <StateTemplatevariable objectReference="modelValue_6"/>
      <StateTemplatevariable objectReference="modelValue_7"/>
      <StateTemplatevariable objectReference="modelValue_8"/>
    </StateTemplate>
    <InitialState type="initialState">
      0 22.9544 0.00155182 0.0001 38.8192950146758 7.62219 0.385859 1 1 0.7798620000000001 0.0001 0.0251133 0.268159 0.390589 6.44406 0.0308656 1.04518 4.20542 
    </InitialState>
  </model>
  <ListOfTasks>
    <Task key="Task_14" name="Steady-State" type="steadyState" scheduled="false" updatemodel="false">
      <Report reference="Report_9" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="JacobianRequested" type="bool" value="1"/>
        <Parameter name="StabilityAnalysisRequested" type="bool" value="1"/>
      </Problem>
      <method name="Enhanced Newton" type="EnhancedNewton">
        <Parameter name="Resolution" type="unsignedFloat" value="1e-009"/>
        <Parameter name="Derivation Factor" type="unsignedFloat" value="0.001"/>
        <Parameter name="Use Newton" type="bool" value="1"/>
        <Parameter name="Use Integration" type="bool" value="1"/>
        <Parameter name="Use Back Integration" type="bool" value="1"/>
        <Parameter name="Accept Negative Concentrations" type="bool" value="0"/>
        <Parameter name="Iteration Limit" type="unsignedInteger" value="50"/>
        <Parameter name="maximum duration for forward integration" type="unsignedFloat" value="1000000000"/>
        <Parameter name="maximum duration for backward integration" type="unsignedFloat" value="1000000"/>
      </method>
    </Task>
    <Task key="Task_15" name="Time-Course" type="timeCourse" scheduled="false" updatemodel="false">
      <Report reference="Report_18" target="" append="0" confirmOverwrite="0"/>
      <Problem>
        <Parameter name="StepNumber" type="unsignedInteger" value="50"/>
        <Parameter name="StepSize" type="float" value="100"/>
        <Parameter name="Duration" type="float" value="5000"/>
        <Parameter name="TimeSeriesRequested" type="bool" value="1"/>
        <Parameter name="OutputStartTime" type="float" value="0"/>
        <Parameter name="Output Event" type="bool" value="0"/>
        <Parameter name="Continue on Simultaneous Events" type="bool" value="0"/>
      </Problem>
      <method name="Deterministic (LSODA)" type="Deterministic(LSODA)">
        <Parameter name="Integrate Reduced model" type="bool" value="0"/>
        <Parameter name="Relative tolerance" type="unsignedFloat" value="1e-006"/>
        <Parameter name="Absolute tolerance" type="unsignedFloat" value="1e-012"/>
        <Parameter name="Max Internal Steps" type="unsignedInteger" value="10000"/>
      </method>
    </Task>
    <Task key="Task_16" name="Scan" type="scan" scheduled="true" updatemodel="false">
      <Report reference="Report_19" target="PEdata.txt" append="0" confirmOverwrite="0"/>
      <Problem>
        <Parameter name="Subtask" type="unsignedInteger" value="5"/>
        <ParameterGroup name="ScanItems">
          <ParameterGroup name="ScanItem">
            <Parameter name="Number of steps" type="unsignedInteger" value="3"/>
            <Parameter name="Object" type="cn" value="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Endosome],Vector=metabolites[ligand receptor complex-endosome],Reference=InitialConcentration"/>
            <Parameter name="Type" type="unsignedInteger" value="0"/>
          </ParameterGroup>
        </ParameterGroup>
        <Parameter name="Output in subtask" type="bool" value="0"/>
        <Parameter name="Adjust initial conditions" type="bool" value="0"/>
      </Problem>
      <method name="Scan Framework" type="ScanFramework">
      </method>
    </Task>
    <Task key="Task_17" name="Elementary Flux modes" type="fluxmode" scheduled="false" updatemodel="false">
      <Report reference="Report_10" target="" append="1" confirmOverwrite="1"/>
      <Problem>
      </Problem>
      <method name="EFM Algorithm" type="EFMAlgorithm">
      </method>
    </Task>
    <Task key="Task_18" name="Optimization" type="optimization" scheduled="false" updatemodel="false">
      <Report reference="Report_11" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="Subtask" type="cn" value="CN=Root,Vector=TaskList[Steady-State]"/>
        <ParameterText name="ObjectiveExpression" type="expression">
          
        </ParameterText>
        <Parameter name="Maximize" type="bool" value="0"/>
        <Parameter name="Randomize Start Values" type="bool" value="0"/>
        <Parameter name="Calculate Statistics" type="bool" value="1"/>
        <ParameterGroup name="OptimizationItemList">
        </ParameterGroup>
        <ParameterGroup name="OptimizationConstraintList">
        </ParameterGroup>
      </Problem>
      <method name="Random Search" type="RandomSearch">
        <Parameter name="Number of Iterations" type="unsignedInteger" value="100000"/>
        <Parameter name="Random Number Generator" type="unsignedInteger" value="1"/>
        <Parameter name="seed" type="unsignedInteger" value="0"/>
      </method>
    </Task>
    <Task key="Task_19" name="Parameter Estimation" type="parameterFitting" scheduled="false" updatemodel="false">
      <Report reference="Report_12" target="" append="0" confirmOverwrite="0"/>
      <Problem>
        <Parameter name="Maximize" type="bool" value="0"/>
        <Parameter name="Randomize Start Values" type="bool" value="1"/>
        <Parameter name="Calculate Statistics" type="bool" value="0"/>
        <ParameterGroup name="OptimizationItemList">
        </ParameterGroup>
        <ParameterGroup name="OptimizationConstraintList">
        </ParameterGroup>
        <Parameter name="Steady-State" type="cn" value="CN=Root,Vector=TaskList[Steady-State]"/>
        <Parameter name="Time-Course" type="cn" value="CN=Root,Vector=TaskList[Time-Course]"/>
        <Parameter name="Create Parameter Sets" type="bool" value="0"/>
        <ParameterGroup name="Experiment Set">
        </ParameterGroup>
        <ParameterGroup name="Validation Set">
          <Parameter name="Threshold" type="unsignedInteger" value="5"/>
          <Parameter name="Weight" type="unsignedFloat" value="1"/>
        </ParameterGroup>
      </Problem>
      <method name="Genetic Algorithm" type="GeneticAlgorithm">
        <Parameter name="Number of Generations" type="unsignedInteger" value="10"/>
        <Parameter name="Population Size" type="unsignedInteger" value="10"/>
        <Parameter name="Random Number Generator" type="unsignedInteger" value="1"/>
        <Parameter name="seed" type="unsignedInteger" value="0"/>
      </method>
    </Task>
    <Task key="Task_20" name="Metabolic Control Analysis" type="metabolicControlAnalysis" scheduled="false" updatemodel="false">
      <Report reference="Report_13" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="Steady-State" type="key" value="Task_14"/>
      </Problem>
      <method name="MCA method (Reder)" type="MCAmethod(Reder)">
        <Parameter name="Modulation Factor" type="unsignedFloat" value="1e-009"/>
        <Parameter name="Use Reeder" type="bool" value="1"/>
        <Parameter name="Use Smallbone" type="bool" value="1"/>
      </method>
    </Task>
    <Task key="Task_21" name="Lyapunov Exponents" type="lyapunovExponents" scheduled="false" updatemodel="false">
      <Report reference="Report_14" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="ExponentNumber" type="unsignedInteger" value="3"/>
        <Parameter name="DivergenceRequested" type="bool" value="1"/>
        <Parameter name="TransientTime" type="float" value="0"/>
      </Problem>
      <method name="Wolf method" type="Wolfmethod">
        <Parameter name="Orthonormalization Interval" type="unsignedFloat" value="1"/>
        <Parameter name="Overall time" type="unsignedFloat" value="1000"/>
        <Parameter name="Relative tolerance" type="unsignedFloat" value="1e-006"/>
        <Parameter name="Absolute tolerance" type="unsignedFloat" value="1e-012"/>
        <Parameter name="Max Internal Steps" type="unsignedInteger" value="10000"/>
      </method>
    </Task>
    <Task key="Task_22" name="Time scale Separation Analysis" type="timescaleSeparationAnalysis" scheduled="false" updatemodel="false">
      <Report reference="Report_15" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="StepNumber" type="unsignedInteger" value="100"/>
        <Parameter name="StepSize" type="float" value="0.01"/>
        <Parameter name="Duration" type="float" value="1"/>
        <Parameter name="TimeSeriesRequested" type="bool" value="1"/>
        <Parameter name="OutputStartTime" type="float" value="0"/>
      </Problem>
      <method name="ILDM (LSODA,Deuflhard)" type="TimescaleSeparation(ILDM,Deuflhard)">
        <Parameter name="Deuflhard tolerance" type="unsignedFloat" value="1e-006"/>
      </method>
    </Task>
    <Task key="Task_23" name="Sensitivities" type="sensitivities" scheduled="false" updatemodel="false">
      <Report reference="Report_16" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="SubtaskType" type="unsignedInteger" value="1"/>
        <ParameterGroup name="TargetFunctions">
          <Parameter name="SingleObject" type="cn" value=""/>
          <Parameter name="ObjectListType" type="unsignedInteger" value="7"/>
        </ParameterGroup>
        <ParameterGroup name="ListOfvariables">
          <ParameterGroup name="variables">
            <Parameter name="SingleObject" type="cn" value=""/>
            <Parameter name="ObjectListType" type="unsignedInteger" value="41"/>
          </ParameterGroup>
        </ParameterGroup>
      </Problem>
      <method name="Sensitivities method" type="Sensitivitiesmethod">
        <Parameter name="Delta factor" type="unsignedFloat" value="0.001"/>
        <Parameter name="Delta minimum" type="unsignedFloat" value="1e-012"/>
      </method>
    </Task>
    <Task key="Task_24" name="Moieties" type="moieties" scheduled="false" updatemodel="false">
      <Problem>
      </Problem>
      <method name="Householder Reduction" type="Householder">
      </method>
    </Task>
    <Task key="Task_25" name="Cross Section" type="crosssection" scheduled="false" updatemodel="false">
      <Problem>
        <Parameter name="StepNumber" type="unsignedInteger" value="100"/>
        <Parameter name="StepSize" type="float" value="0.01"/>
        <Parameter name="Duration" type="float" value="1"/>
        <Parameter name="TimeSeriesRequested" type="bool" value="1"/>
        <Parameter name="OutputStartTime" type="float" value="0"/>
        <Parameter name="Output Event" type="bool" value="0"/>
        <Parameter name="Continue on Simultaneous Events" type="bool" value="0"/>
        <Parameter name="LimitCrossings" type="bool" value="0"/>
        <Parameter name="NumCrossingsLimit" type="unsignedInteger" value="0"/>
        <Parameter name="LimitOutTime" type="bool" value="0"/>
        <Parameter name="LimitOutCrossings" type="bool" value="0"/>
        <Parameter name="PositiveDirection" type="bool" value="1"/>
        <Parameter name="NumOutCrossingsLimit" type="unsignedInteger" value="0"/>
        <Parameter name="LimitUntilConvergence" type="bool" value="0"/>
        <Parameter name="Convergencetolerance" type="float" value="1e-006"/>
        <Parameter name="Threshold" type="float" value="0"/>
        <Parameter name="DelayOutputUntilConvergence" type="bool" value="0"/>
        <Parameter name="OutputConvergencetolerance" type="float" value="1e-006"/>
        <ParameterText name="TriggerExpression" type="expression">
          
        </ParameterText>
        <Parameter name="Singlevariable" type="cn" value=""/>
      </Problem>
      <method name="Deterministic (LSODA)" type="Deterministic(LSODA)">
        <Parameter name="Integrate Reduced model" type="bool" value="0"/>
        <Parameter name="Relative tolerance" type="unsignedFloat" value="1e-006"/>
        <Parameter name="Absolute tolerance" type="unsignedFloat" value="1e-012"/>
        <Parameter name="Max Internal Steps" type="unsignedInteger" value="10000"/>
      </method>
    </Task>
    <Task key="Task_26" name="Linear Noise Approximation" type="linearNoiseApproximation" scheduled="false" updatemodel="false">
      <Report reference="Report_17" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="Steady-State" type="key" value="Task_14"/>
      </Problem>
      <method name="Linear Noise Approximation" type="LinearNoiseApproximation">
      </method>
    </Task>
  </ListOfTasks>
  <ListOfReports>
    <Report key="Report_9" name="Steady-State" taskType="steadyState" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Footer>
        <Object cn="CN=Root,Vector=TaskList[Steady-State]"/>
      </Footer>
    </Report>
    <Report key="Report_10" name="Elementary Flux modes" taskType="fluxmode" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Footer>
        <Object cn="CN=Root,Vector=TaskList[Elementary Flux modes],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_11" name="Optimization" taskType="optimization" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Object=Description"/>
        <Object cn="String=\[Function Evaluations\]"/>
        <Object cn="separator=&#x09;"/>
        <Object cn="String=\[Best Value\]"/>
        <Object cn="separator=&#x09;"/>
        <Object cn="String=\[Best Parameters\]"/>
      </Header>
      <Body>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Problem=Optimization,Reference=Function Evaluations"/>
        <Object cn="separator=&#x09;"/>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Problem=Optimization,Reference=Best Value"/>
        <Object cn="separator=&#x09;"/>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Problem=Optimization,Reference=Best Parameters"/>
      </Body>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_12" name="Parameter Estimation" taskType="parameterFitting" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Object=Description"/>
        <Object cn="String=\[Function Evaluations\]"/>
        <Object cn="separator=&#x09;"/>
        <Object cn="String=\[Best Value\]"/>
        <Object cn="separator=&#x09;"/>
        <Object cn="String=\[Best Parameters\]"/>
      </Header>
      <Body>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Function Evaluations"/>
        <Object cn="separator=&#x09;"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Value"/>
        <Object cn="separator=&#x09;"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Parameters"/>
      </Body>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_13" name="Metabolic Control Analysis" taskType="metabolicControlAnalysis" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Metabolic Control Analysis],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Metabolic Control Analysis],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_14" name="Lyapunov Exponents" taskType="lyapunovExponents" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Lyapunov Exponents],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Lyapunov Exponents],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_15" name="Time scale Separation Analysis" taskType="timescaleSeparationAnalysis" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Time scale Separation Analysis],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Time scale Separation Analysis],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_16" name="Sensitivities" taskType="sensitivities" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Sensitivities],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Sensitivities],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_17" name="Linear Noise Approximation" taskType="linearNoiseApproximation" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Linear Noise Approximation],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Linear Noise Approximation],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_18" name="Time-Course" taskType="unset" separator="&#x09;" precision="6">
      <Comment>
      </Comment>
      <Table printTitle="1">
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Reference=Time"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Endosome],Vector=metabolites[ligand receptor complex-endosome],Reference=Concentration"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Plasma membrane],Vector=metabolites[Receptor 2],Reference=Concentration"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Endosome],Vector=metabolites[Receptor 1-endosome],Reference=Concentration"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Endosome],Vector=metabolites[Receptor 2 endosome],Reference=Concentration"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Plasma membrane],Vector=metabolites[Receptor 1],Reference=Concentration"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Plasma membrane],Vector=metabolites[ligand receptor complex-plasma membrane],Reference=Concentration"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[pRII],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[kcd],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ka],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ligand],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ki],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[pRI],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[kr],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[alpha],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[klid],Reference=InitialValue"/>
      </Table>
    </Report>
    <Report key="Report_19" name="parameter_estimation" taskType="parameterFitting" separator="&#x09;" precision="6">
      <Comment>
      </Comment>
      <Table printTitle="1">
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Endosome],Vector=metabolites[ligand receptor complex-endosome],Reference=InitialConcentration"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Plasma membrane],Vector=metabolites[Receptor 2],Reference=InitialConcentration"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Endosome],Vector=metabolites[Receptor 1-endosome],Reference=InitialConcentration"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Endosome],Vector=metabolites[Receptor 2 endosome],Reference=InitialConcentration"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Plasma membrane],Vector=metabolites[Receptor 1],Reference=InitialConcentration"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Compartments[Plasma membrane],Vector=metabolites[ligand receptor complex-plasma membrane],Reference=InitialConcentration"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[pRII],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[kcd],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ka],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ligand],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[ki],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[pRI],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[kr],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[alpha],Reference=InitialValue"/>
        <Object cn="CN=Root,model=Vilar2006_TGFbeta,Vector=Values[klid],Reference=InitialValue"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Value"/>
      </Table>
    </Report>
  </ListOfReports>
  <ListOfplots>
    <plotSpecification name="Parameter Estimation Result" type="plot2D" active="1">
      <Parameter name="log x" type="bool" value="0"/>
      <Parameter name="log Y" type="bool" value="0"/>
      <ListOfplotItems>
        <plotItem name="Experiment_0,[ligand receptor complex-endosome](Measured Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#FF0000"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="1"/>
          <Parameter name="Line type" type="unsignedInteger" value="3"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="1"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Measured Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[ligand receptor complex-endosome](Fitted Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#FF0000"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Fitted Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[ligand receptor complex-endosome](Weighted Error)" type="Curve2D">
          <Parameter name="color" type="string" value="#FF0000"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="2"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="2"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Weighted Error"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[Receptor 2](Measured Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#0000FF"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="1"/>
          <Parameter name="Line type" type="unsignedInteger" value="3"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="1"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[1],Reference=Measured Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[Receptor 2](Fitted Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#0000FF"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[1],Reference=Fitted Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[Receptor 2](Weighted Error)" type="Curve2D">
          <Parameter name="color" type="string" value="#0000FF"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="2"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="2"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[1],Reference=Weighted Error"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[Receptor 1-endosome](Measured Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#00E600"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="1"/>
          <Parameter name="Line type" type="unsignedInteger" value="3"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="1"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[2],Reference=Measured Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[Receptor 1-endosome](Fitted Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#00E600"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[2],Reference=Fitted Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[Receptor 1-endosome](Weighted Error)" type="Curve2D">
          <Parameter name="color" type="string" value="#00E600"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="2"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="2"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[2],Reference=Weighted Error"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[Receptor 2 endosome](Measured Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#00BEF0"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="1"/>
          <Parameter name="Line type" type="unsignedInteger" value="3"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="1"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[3],Reference=Measured Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[Receptor 2 endosome](Fitted Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#00BEF0"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[3],Reference=Fitted Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[Receptor 2 endosome](Weighted Error)" type="Curve2D">
          <Parameter name="color" type="string" value="#00BEF0"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="2"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="2"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[3],Reference=Weighted Error"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[Receptor 1](Measured Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#F000FF"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="1"/>
          <Parameter name="Line type" type="unsignedInteger" value="3"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="1"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[4],Reference=Measured Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[Receptor 1](Fitted Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#F000FF"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[4],Reference=Fitted Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[Receptor 1](Weighted Error)" type="Curve2D">
          <Parameter name="color" type="string" value="#F000FF"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="2"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="2"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[4],Reference=Weighted Error"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[ligand receptor complex-plasma membrane](Measured Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#F0C800"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="1"/>
          <Parameter name="Line type" type="unsignedInteger" value="3"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="1"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[5],Reference=Measured Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[ligand receptor complex-plasma membrane](Fitted Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#F0C800"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[5],Reference=Fitted Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment_0,[ligand receptor complex-plasma membrane](Weighted Error)" type="Curve2D">
          <Parameter name="color" type="string" value="#F0C800"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="2"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="2"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[5],Reference=Weighted Error"/>
          </ListOfChannels>
        </plotItem>
      </ListOfplotItems>
    </plotSpecification>
    <plotSpecification name="Parameter Estimation Result_1" type="plot2D" active="1">
      <Parameter name="log x" type="bool" value="0"/>
      <Parameter name="log Y" type="bool" value="0"/>
      <ListOfplotItems>
        <plotItem name="Experiment,[ligand receptor complex-endosome](Measured Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#FF0000"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="1"/>
          <Parameter name="Line type" type="unsignedInteger" value="3"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="1"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Measured Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[ligand receptor complex-endosome](Fitted Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#FF0000"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Fitted Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[ligand receptor complex-endosome](Weighted Error)" type="Curve2D">
          <Parameter name="color" type="string" value="#FF0000"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="2"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="2"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Weighted Error"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[Receptor 2](Measured Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#0000FF"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="1"/>
          <Parameter name="Line type" type="unsignedInteger" value="3"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="1"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[1],Reference=Measured Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[Receptor 2](Fitted Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#0000FF"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[1],Reference=Fitted Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[Receptor 2](Weighted Error)" type="Curve2D">
          <Parameter name="color" type="string" value="#0000FF"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="2"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="2"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[1],Reference=Weighted Error"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,Receptor 1-endosome.ParticleNumber(Measured Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#00E600"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="1"/>
          <Parameter name="Line type" type="unsignedInteger" value="3"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="1"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[2],Reference=Measured Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,Receptor 1-endosome.ParticleNumber(Fitted Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#00E600"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[2],Reference=Fitted Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,Receptor 1-endosome.ParticleNumber(Weighted Error)" type="Curve2D">
          <Parameter name="color" type="string" value="#00E600"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="2"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="2"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[2],Reference=Weighted Error"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[Receptor 2 endosome](Measured Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#00BEF0"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="1"/>
          <Parameter name="Line type" type="unsignedInteger" value="3"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="1"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[3],Reference=Measured Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[Receptor 2 endosome](Fitted Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#00BEF0"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[3],Reference=Fitted Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[Receptor 2 endosome](Weighted Error)" type="Curve2D">
          <Parameter name="color" type="string" value="#00BEF0"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="2"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="2"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[3],Reference=Weighted Error"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[Receptor 2 endosome](Measured Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#F000FF"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="1"/>
          <Parameter name="Line type" type="unsignedInteger" value="3"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="1"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[4],Reference=Measured Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[Receptor 2 endosome](Fitted Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#F000FF"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[4],Reference=Fitted Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[Receptor 2 endosome](Weighted Error)" type="Curve2D">
          <Parameter name="color" type="string" value="#F000FF"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="2"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="2"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[4],Reference=Weighted Error"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[Receptor 1](Measured Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#F0C800"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="1"/>
          <Parameter name="Line type" type="unsignedInteger" value="3"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="1"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[5],Reference=Measured Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[Receptor 1](Fitted Value)" type="Curve2D">
          <Parameter name="color" type="string" value="#F0C800"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[5],Reference=Fitted Value"/>
          </ListOfChannels>
        </plotItem>
        <plotItem name="Experiment,[Receptor 1](Weighted Error)" type="Curve2D">
          <Parameter name="color" type="string" value="#F0C800"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="2"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="after"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="2"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[0],Reference=Independent Value"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,ParameterGroup=Experiment Set,ParameterGroup=Experiment,Vector=Fitted Points[5],Reference=Weighted Error"/>
          </ListOfChannels>
        </plotItem>
      </ListOfplotItems>
    </plotSpecification>
    <plotSpecification name="Progress of Fit" type="plot2D" active="1">
      <Parameter name="log x" type="bool" value="0"/>
      <Parameter name="log Y" type="bool" value="1"/>
      <ListOfplotItems>
        <plotItem name="sum of squares" type="Curve2D">
          <Parameter name="color" type="string" value="auto"/>
          <Parameter name="Line subtype" type="unsignedInteger" value="0"/>
          <Parameter name="Line type" type="unsignedInteger" value="0"/>
          <Parameter name="Line width" type="unsignedFloat" value="1"/>
          <Parameter name="Recording Activity" type="string" value="during"/>
          <Parameter name="Symbol subtype" type="unsignedInteger" value="0"/>
          <ListOfChannels>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Function Evaluations"/>
            <ChannelSpec cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Value"/>
          </ListOfChannels>
        </plotItem>
      </ListOfplotItems>
    </plotSpecification>
  </ListOfplots>
  <GUI>
  </GUI>
  <SBMLReference file="Vilar2006_TGFbeta.xml">
    <SBMLMap SBMLid="Endosome" COPASIkey="Compartment_3"/>
    <SBMLMap SBMLid="PM" COPASIkey="Compartment_1"/>
    <SBMLMap SBMLid="RI" COPASIkey="Metabolite_1"/>
    <SBMLMap SBMLid="RII" COPASIkey="Metabolite_3"/>
    <SBMLMap SBMLid="RII_endo" COPASIkey="Metabolite_11"/>
    <SBMLMap SBMLid="RI_endo" COPASIkey="Metabolite_9"/>
    <SBMLMap SBMLid="alpha" COPASIkey="modelValue_7"/>
    <SBMLMap SBMLid="ka" COPASIkey="modelValue_0"/>
    <SBMLMap SBMLid="kcd" COPASIkey="modelValue_2"/>
    <SBMLMap SBMLid="ki" COPASIkey="modelValue_4"/>
    <SBMLMap SBMLid="klid" COPASIkey="modelValue_3"/>
    <SBMLMap SBMLid="kr" COPASIkey="modelValue_6"/>
    <SBMLMap SBMLid="lRIRII" COPASIkey="Metabolite_5"/>
    <SBMLMap SBMLid="lRIRII_endo" COPASIkey="Metabolite_7"/>
    <SBMLMap SBMLid="ligand" COPASIkey="modelValue_1"/>
    <SBMLMap SBMLid="pRI" COPASIkey="modelValue_5"/>
    <SBMLMap SBMLid="pRII" COPASIkey="modelValue_8"/>
    <SBMLMap SBMLid="v1" COPASIkey="Reaction_0"/>
    <SBMLMap SBMLid="v10" COPASIkey="Reaction_9"/>
    <SBMLMap SBMLid="v11" COPASIkey="Reaction_10"/>
    <SBMLMap SBMLid="v12" COPASIkey="Reaction_11"/>
    <SBMLMap SBMLid="v13" COPASIkey="Reaction_12"/>
    <SBMLMap SBMLid="v2" COPASIkey="Reaction_1"/>
    <SBMLMap SBMLid="v3" COPASIkey="Reaction_2"/>
    <SBMLMap SBMLid="v4" COPASIkey="Reaction_3"/>
    <SBMLMap SBMLid="v5" COPASIkey="Reaction_4"/>
    <SBMLMap SBMLid="v6" COPASIkey="Reaction_5"/>
    <SBMLMap SBMLid="v7" COPASIkey="Reaction_6"/>
    <SBMLMap SBMLid="v8" COPASIkey="Reaction_7"/>
    <SBMLMap SBMLid="v9" COPASIkey="Reaction_8"/>
  </SBMLReference>
</COPASI>

'''


class ProfileLikelihoodTestsindex0(unittest.TestCase):
    '''
    tests where PE is conducted and index is 0
    '''
    
    
    def setUp(self):
        copasi_file=os.path.join(os.getcwd(),'Vilarmodel2006pycopitestmodel.cps')
        if os.path.isfile(copasi_file):
            os.remove(copasi_file)
        with open(copasi_file,'w') as f:
            f.write(model_string)
            
        self.copasi_file=copasi_file
        self.timecourse_report_name=os.path.join(os.getcwd(),'timecourse.txt')
        if os.path.isfile(self.timecourse_report_name):
            os.remove(self.timecourse_report_name)
            
        self.PE_report_name=os.path.join(os.path.dirname(self.copasi_file),'PEdata.txt')
        self.TC=PyCoTools.pycopi.TimeCourse(self.copasi_file,StepSize=100,plot='false',Intervals=50,End=5000,report_name=self.timecourse_report_name)
        PyCoTools.pycopi.PruneCopasiHeaders(self.timecourse_report_name,replace='true')
        
        self.PE=PyCoTools.pycopi.ParameterEstimation(self.copasi_file,
                                                        self.timecourse_report_name,
                                                        population_size=6,
                                                        number_of_generations=5,
                                                        randomize_start_values='true',
                                                        report_name=self.PE_report_name,
                                                        save='overwrite',plot='false',
                                                        run='false')
        self.PE.write_item_template()
        self.PE.set_up()
                                                        
        self.S=PyCoTools.pycopi.Scan(self.copasi_file,scan_type='repeat',
                                        report_type='parameter_estimation',
                                        run='true',number_of_steps=3,
                                        report_name=self.PE_report_name,scheduled='true')

#        self.PE.run()
        self.PE_dir=os.path.join(os.path.dirname(self.copasi_file),'PE_dir')
        if os.path.isdir(self.PE_dir)==False:
            os.mkdir(self.PE_dir)
        new_fle= os.path.join(self.PE_dir,os.path.split(self.PE_report_name)[1])
        shutil.copy(self.PE_report_name,new_fle)
        
        PyCoTools.pycopi.PruneCopasiHeaders(new_fle,replace='true')
        
        self.PL=PyCoTools.pydentify2.ProfileLikelihood(self.copasi_file,
                                                       parameter_path=self.PE_report_name,
                                                       index=0,iteration_limit=10,
                                                       run='false',
                                                       upper_boundMultiplier=1000,
                                                       lower_boundMultiplier=1000)
        self.GMQ=PyCoTools.pycopi.GetModelQuantities(self.copasi_file)


    def test_index_is_0(self):
        self.assertEqual(self.PL.cps_dct.keys()[0],0)
        
    def test_insert_parameters(self):
        input_parameters= pandas.DataFrame(self.PL.PE_data.iloc[self.PL.kwargs.get('index')]).transpose()
        for i in self.PL.cps_dct[0].keys():
            GMQ=PyCoTools.pycopi.GetModelQuantities(self.PL.cps_dct[0][i])
            model_val = float(GMQ.get_all_params_dict()[i])
            input_val= float(input_parameters[i])
            self.assertAlmostEqual(model_val,input_val)
        
    def test_copy_files(self):
        [self.assertTrue(i) for i in self.PL.cps_dct[0]]
        
    def test_fit_items(self):
        key= self.PL.cps_dct[0].keys()[4]
        val= self.PL.cps_dct[0][key]
        copasiML=PyCoTools.pycopi.CopasiMLParser(val).copasiML
        GMQ=PyCoTools.pycopi.GetModelQuantities(val)
        key_cn= GMQ.get_all_model_variables()[key]['cn']
#        print copasiML
        l=[]
        query="//*[@name='FitItem']" 
        for i in copasiML.xpath(query):
            for j in  list(i):
                if j.attrib['name']=='ObjectCN':
                    match= re.findall('.*\]',j.attrib['value'])[0]
                    l.append(match)
        self.assertNotIn(key_cn,l)
        
    def test_x(self):
        key= self.PL.cps_dct[0].keys()[4]
        val= self.PL.cps_dct[0][key]
        copasiML=PyCoTools.pycopi.CopasiMLParser(val).copasiML
        GMQ=PyCoTools.pycopi.GetModelQuantities(val)
#        key_cn= GMQ.get_all_model_variables()[key]['cn']     
        
        query="//*[@name='FitItem']" 
        for i in copasiML.xpath(query):
            for j in list(i):
                print j.attrib
        
    def tearDown(self):
        os.remove(self.copasi_file)
        os.remove(self.PE_report_name)
        shutil.rmtree(self.PE_dir)
        for i in glob.glob('*.pickle'):
            os.remove(i)            
        os.remove(self.PE.kwargs.get('ItemTemplateFilename'))
        os.remove(self.timecourse_report_name)
#        import time
#        time.sleep(1)
#        shutil.rmtree(self.PL.IA_dir)
        



        
#        if os.path.isdir(self.PE_dir):
#            shutil.rmtree(self.PE_dir)
##        if os.path.isfile(self.copasi_file):
##            os.remove(self.copasi_file)
#
#        if os.path.isfile(self.timecourse_report_name):
#            os.remove(self.timecourse_report_name)
#
#        for i in glob.glob('*.jpeg'):
#            os.remove(i)
#            
#        for i in glob.glob('*.xlsx'):
#            os.remove(i)
#








            
##==============================================================================
#
#class ParsePETests(unittest.TestCase):
#    
#    def find_cps(self):
#        assert glob.glob('*.cps')
#        cps=glob.glob('*.cps')[0]
#        return os.path.join(os.getcwd(),cps)
#        
#    def find_PE_data_file(self):
#        for i in glob.glob('PE.txt'):
#            path= os.path.join(os.getcwd(),i)
#            assert os.path.isfile(path)
#            return path
#
#
#    def find_PE_data_folder(self):
#        for i in os.listdir(os.getcwd()):
#            assert os.path.isdir('Results'),'No folder called results containing PE results in current directory. run some parameter estimations'
#            return os.path.join(os.getcwd(),'Results')
#            
#    def setUp(self):
#        self.copasi_file=self.find_cps()
#        self.PE_file=self.find_PE_data_file()
#        self.PE_dir=self.find_PE_data_folder()
#        
#    def test_mode_file(self):
#        PED= ParsePEData(self.PE_file)
#        self.assertEqual( PED.mode,'file')
#        
#    def test_mode_folder(self):
#        PED= ParsePEData(self.PE_dir)
#        self.assertEqual( PED.mode,'folder')    
#        
#    def test_read_file(self):
#        PED=ParsePEData(self.PE_file)
#        data= PED.read_file()
#        self.assertTrue(isinstance(data,pandas.core.frame.DataFrame))
#
#    def test_read_folder(self):
#        PED=ParsePEData(self.PE_dir)
#        data= PED.read_folder()
#        self.assertTrue(isinstance(data,pandas.core.frame.DataFrame))
#
#    def test_rename_RSS(self):
#        PED=ParsePEData(self.PE_dir)
#        self.assertIn('RSS', PED.data.keys())
#        
#        
#    def test_sort(self):
#        PED=ParsePEData(self.PE_dir)
#        self.assertTrue( all(PED.data['RSS'][i]<= PED.data['RSS'][i+1] for i in range(PED.data['RSS'].shape[0]-1)))
#        
#    def test_read_data_from_dir(self):
#        PED=ParsePEData(self.PE_dir)
#        self.assertTrue(isinstance(PED.read_data(),pandas.core.frame.DataFrame))
#
#
#    def test_read_data_from_file(self):
#        PED=ParsePEData(self.PE_file)
#        self.assertTrue(isinstance(PED.read_data(),pandas.core.frame.DataFrame))
#        
#    def test_read_data_from_pickle_true_overwrite_pickle_false(self):
#        PED=ParsePEData(self.PE_dir,from_pickle=True,overwrite_pickle=False)
#        self.assertTrue(isinstance( PED.read_data(),pandas.core.frame.DataFrame))
#
#    def test_read_data_from_pickle_true_overwrite_pickle_true(self):
#        PED=ParsePEData(self.PE_dir,from_pickle=True,overwrite_pickle=True)
#        self.assertTrue(isinstance( PED.read_data(),pandas.core.frame.DataFrame))
#        
#    def test_read_data_from_pickle_false_overwrite_pickle_true(self):
#        PED=ParsePEData(self.PE_dir,from_pickle=False,overwrite_pickle=True)
#        self.assertTrue(isinstance( PED.read_data(),pandas.core.frame.DataFrame))
#
#    def test_read_data_from_pickle_false_overwrite_pickle_false(self):
#        PED=ParsePEData(self.PE_dir,from_pickle=False,overwrite_pickle=False)
#        self.assertTrue(isinstance( PED.read_data(),pandas.core.frame.DataFrame))
#                      
##    def test_pickle_data_frompickle_false(self):
##        PED=ParsePEData(self.PE_dir,from_pickle=False)
##        print PED.write_pickle(PED.read_folder())
##        if os.path.isfile(PED.pickle_path):
##            os.remove(PED.pickle_path)
##        PED.write_pickle(PED.read_folder()) 
##        self.assertTrue(os.path.isfile(PED.pickle_path))
#        
#    def tearDown(self):
#        PED=ParsePEData(self.PE_dir)
#        #delete pickle path
#        if os.path.isfile(PED.pickle_path):
#            os.remove(PED.pickle_path)
#
##==============================================================================
#class InsertParameterTests(unittest.TestCase):
#    def find_cps(self):
#        assert glob.glob('*.cps')
#        cps=glob.glob('*.cps')[0]
#        return os.path.join(os.getcwd(),cps)
#        
#    def find_PE_data_file(self):
#        for i in glob.glob('PE.txt'):
#            path= os.path.join(os.getcwd(),i)
#            assert os.path.isfile(path)
#            return path
#
#
#    def find_PE_data_folder(self):
#        for i in os.listdir(os.getcwd()):
#            assert os.path.isdir('Results'),'No folder called results containing PE results in current directory. run some parameter estimations'
#            return os.path.join(os.getcwd(),'Results')
#            
#    def setUp(self):
#        self.copasi_file=self.find_cps()
#        self.PE_file=self.find_PE_data_file()
#        self.PE_dir=self.find_PE_data_folder()    
#
#
#    def test_convert_molar_to_particles(self):
#        GMQ=GetModelQuantities(self.copasi_file)
#        print GMQ


#==============================================================================


if __name__=='__main__':
#    current_dir= os.getcwd()    
#    new_dir= os.path.join(os.getcwd(),r'Tests\Pydentify2Tests')
#    os.chdir(new_dir)

    unittest.main()
    
























