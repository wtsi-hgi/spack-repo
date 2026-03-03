# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkconverter(RPackage):
	"""The Parameter Converter of the Pharmacokinetic Models

	Pharmacokinetics is the study of drug absorption, distribution, 
   metabolism, and excretion. The pharmacokinetics model explains that how the 
   drug concentration change as the drug moves through the different compartments
   of the body. For pharmacokinetic modeling and analysis, it is essential
   to understand the basic pharmacokinetic parameters. All parameters are 
   considered, but only some of parameters are used in the model. Therefore, 
   we need to convert the estimated parameters to the other parameters after 
   fitting the specific pharmacokinetic model. This package is developed to help
   this converting work. For more detailed explanation of pharmacokinetic 
   parameters, see "Gabrielsson and Weiner" (2007), "ISBN-10: 9197651001";
   "Benet and Zia-Amirhosseini" (1995) <DOI: 10.1177/019262339502300203>; 
   "Mould and Upton" (2012) <DOI: 10.1038/psp.2012.4>;
   "Mould and Upton" (2013) <DOI: 10.1038/psp.2013.14>.
	"""
	
	cran = "PKconverter" 

	version("1.5", md5="a2a047ee68cbd8c4f3d034b81e059f01")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
