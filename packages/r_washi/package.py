# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWashi(RPackage):
	"""Washington Soil Health Initiative Branding

	Create plots and tables in a consistent style with WaSHI
    (Washington Soil Health Initiative) branding. Use 'washi' to easily
    style your 'ggplot2' plots and 'flextable' tables.
	"""
	
	homepage = "https://github.com/WA-Department-of-Agriculture/washi"
	cran = "washi" 

	version("0.2.0", md5="7fabba3338ab22abe529fdfa00f701aa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-systemfonts", type=("build", "run"))
