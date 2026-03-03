# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmanida(RPackage):
	"""Meta-Analysis for Non-Integral Data

	Combination of results for meta-analysis using significance
    and effect size only. P-values and fold-change are combined to obtain
    a global significance on each metabolite. Produces a volcano plot
    summarising the relevant results from meta-analysis. Vote-counting
    reports for metabolites. And explore plot to detect discrepancies
    between studies at a first glance. Methodology is described in the
    Llambrich et al. (2021) <doi:10.1093/bioinformatics/btab591>.  
	"""
	
	homepage = "https://github.com/mariallr/amanida"
	cran = "amanida" 

	version("0.3.0", md5="be6db8bad1f3eddab93f61dba55c8167")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggrepel@0.9:", type=("build", "run"))
	depends_on("r-kableextra@1.3:", type=("build", "run"))
	depends_on("r-knitr@1.45:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-readr@1:", type=("build", "run"))
	depends_on("r-readxl@1:", type=("build", "run"))
	depends_on("r-rmarkdown@2.25:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-tidyverse@1.3:", type=("build", "run"))
	depends_on("r-webchem@1.1:", type=("build", "run"))
