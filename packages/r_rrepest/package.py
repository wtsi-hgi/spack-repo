# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrepest(RPackage):
	"""An Analyzer of International Large Scale Assessments in
Education

	A fast way to analyze International Large-Scale Assessments (ILSAs) or any other dataset 
  that includes replicated weights (Balanced Repeated Replication (BRR) weights, Jackknife replicate weights,...) and/or plausible values.
  'Rrepest' contains functionalities that enable you to calculate basic statistics (means, correlations, etc.),
  frequencies, linear regression, or any other model already implemented in R that takes a data frame and weights
  as parameters. It also includes options to prepare the results for publication, following the table formatting standards of the 
  Organization for Economic Cooperation and Development (OECD).
	"""
	
	cran = "Rrepest" 

	version("1.3.0", md5="166c284a191e1dd5bf41b744a6be983a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
	depends_on("r-doparallel@1.0.17:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-flextable@0.7.2:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-labelled@2.9.1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-officer@0.6.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-tibble@3.1.8:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
