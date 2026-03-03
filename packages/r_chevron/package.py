# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChevron(RPackage):
	"""Standard TLGs for Clinical Trials Reporting

	Provide standard tables, listings, and graphs (TLGs) libraries used in
    clinical trials. This package implements a structure to reformat the data with
    'dunlin', create reporting tables using 'rtables' and 'tern' with standardized
    input arguments to enable quick generation of standard outputs.
    In addition, it also provides comprehensive data checks and script generation functionality.
	"""
	
	homepage = "https://insightsengineering.github.io/chevron/"
	cran = "chevron" 

	version("0.2.5", md5="d6b1d91fb2d297ff59c62380632b4624")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-dunlin@0.1.7:", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-formatters@0.5.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-glue@1:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-nestcolor@0.1.1:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-rlistings@0.2.7:", type=("build", "run"))
	depends_on("r-rtables@0.6.6:", type=("build", "run"))
	depends_on("r-stringr@1.4.1:", type=("build", "run"))
	depends_on("r-tern@0.9.3:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
