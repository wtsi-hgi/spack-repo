# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMalan(RPackage):
	"""MAle Lineage ANalysis

	MAle Lineage ANalysis by simulating 
    genealogies backwards and imposing short tandem repeats (STR) mutations forwards. 
    Intended for forensic Y chromosomal STR (Y-STR) haplotype analyses. 
    Numerous analyses are possible, e.g. number of matches and meiotic distance to matches. 
    Refer to papers mentioned in citation("malan") (DOI's: 
    <doi:10.1371/journal.pgen.1007028>, 
    <doi:10.21105/joss.00684> and 
    <doi:10.1016/j.fsigen.2018.10.004>).
	"""
	
	cran = "malan" 

	version("1.0.3", md5="cca6ebde8913ffd2c64c8d2c6f0aa3af")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.7.3:", type=("build", "run"))
	depends_on("r-tidygraph@1.0.0.9999:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-tibble@1.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
