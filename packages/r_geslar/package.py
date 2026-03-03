# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeslar(RPackage):
	"""Get and Manipulate the GESLA Dataset

	Promote access to the GESLA
    <https://gesla787883612.wordpress.com> (Global Extreme Sea Level
    Analysis) dataset, a higher-frequency sea-level record data from all
    over the world. It provides functions to download it entirely, or
    query subsets directly into R, without the need of downloading the
    full dataset. Also, it provides a built-in web-application, so that
    users can apply basic filters to select the data of interest,
    generating informative plots, and showing the selected sites.
	"""
	
	homepage = "https://github.com/EireExtremes/geslaR"
	cran = "geslaR" 

	version("1.0-1", md5="675915aec9437af647c1787793515ff3")

	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("arrow", type=("build", "link", "run"))
