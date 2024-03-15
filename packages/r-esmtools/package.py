# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsmtools(RPackage):
	"""Preprocessing Experience Sampling Method (ESM) Data

	Tailored explicitly for Experience Sampling Method (ESM)
    data, it contains a suite of functions designed to simplify
    preprocessing steps and create subsequent reporting. It empowers
    users with capabilities to extract critical insights during
    preprocessing, conducts thorough data quality assessments (e.g., design
    and sampling scheme checks, compliance rate, careless responses), and
    generates visualizations and concise summary tables tailored
    specifically for ESM data. Additionally, it streamlines the creation
    of informative and interactive preprocessing reports, enabling
    researchers to transparently share their dataset preprocessing
    methodologies. Finally, it is part of a larger ecosystem which
    includes a framework and a web gallery
    (<https://preprocess.esmtools.com/>).
	"""
	
	homepage = "https://gitlab.kuleuven.be/ppw-okpiv/researchers/u0148925/esmtools/"
	cran = "esmtools" 

	version("1.0.1", md5="effec2416626a8a7bb73fd1438dc8427")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-base64enc@0.1.3:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-dt@0.28:", type=("build", "run"))
	depends_on("r-fs@1.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggpubr@0.6:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite@1.8:", type=("build", "run"))
	depends_on("r-kableextra@1.3:", type=("build", "run"))
	depends_on("r-knitr@1.43:", type=("build", "run"))
	depends_on("r-lubridate@1.9:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
