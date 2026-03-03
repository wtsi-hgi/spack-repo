# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuperb(RPackage):
	"""Summary Plots with Adjusted Error Bars

	
    Computes standard error and confidence interval of various descriptive statistics under 
    various designs and sampling schemes. The main function, superbPlot(), return a plot. superbData() 
    returns a dataframe with the statistic and its precision interval so that other plotting package
    can be used. See Cousineau and colleagues (2021) <doi:10.1177/25152459211035109> 
    or Cousineau (2017) <doi:10.5709/acp-0214-z> for a review as well as Cousineau (2005)
    <doi:10.20982/tqmp.01.1.p042>, Morey (2008) <doi:10.20982/tqmp.04.2.p061>, Baguley (2012)
    <doi:10.3758/s13428-011-0123-7>, Cousineau & Laurencelle (2016) <doi:10.1037/met0000055>,
    Cousineau & O'Brien (2014) <doi:10.3758/s13428-013-0441-z>, Calderini & Harding 
    <doi:10.20982/tqmp.15.1.p001> for specific references.
	"""
	
	homepage = "https://dcousin3.github.io/superb/"
	cran = "superb" 

	version("0.95.9", md5="8225a57b3ad472531574dc5e1af53c69")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lsr@0.5:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
