# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgvgd(RPackage):
	"""An R Implementation of the 'Align-GVGD' Method

	'Align-GVGD' ('A-GVGD') is a method to predict the impact of
    'missense' substitutions based on the properties of amino acid side
    chains and protein multiple sequence alignments
    <doi:10.1136/jmg.2005.033878>. 'A-GVGD' is an extension of the original
    'Grantham' distance to multiple sequence alignments. This package
    provides an alternative R implementation to the web version found on
    <http://agvgd.hci.utah.edu/>.
	"""
	
	homepage = "https://maialab.org/agvgd/"
	cran = "agvgd" 

	version("0.1.2", md5="3ac04d872e169f564c9aab647d257df9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-grantham", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
