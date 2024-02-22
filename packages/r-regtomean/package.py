# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegtomean(RPackage):
	"""Regression Toward the Mean

	In repeated measures studies with extreme large or small values it is common 
  that the subjects measurements on average are closer to the mean of the basic population. 
  Interpreting possible changes in the mean in such situations can lead to biased results 
  since the values were not randomly selected, they come from truncated sampling.
  This method allows to estimate the range of means where treatment effects are likely to occur 
  when regression toward the mean is present. 
  Ostermann, T., Willich, Stefan N. & Luedtke, Rainer. (2008). Regression toward the mean - a detection method for unknown population mean based on Mee and Chua's algorithm. BMC Medical Research Methodology.<doi:10.1186/1471-2288-8-52>.
	"""
	
	cran = "regtomean" 

	version("1.1", md5="87eea7950578ccef6f38cc4447a2e4c9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
	depends_on("r-effsize", type=("build", "run"))
	depends_on("r-mefa", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-sjplot", type=("build", "run"))
	depends_on("r-sjmisc", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
