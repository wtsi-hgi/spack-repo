# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpencpu(RPackage):
	"""Producing and Reproducing Results

	A system for embedded scientific computing and reproducible research with R.
    The OpenCPU server exposes a simple but powerful HTTP api for RPC and data interchange
    with R. This provides a reliable and scalable foundation for statistical services or 
    building R web applications. The OpenCPU server runs either as a single-user development
    server within the interactive R session, or as a multi-user Linux stack based on Apache2. 
    The entire system is fully open source and permissively licensed. The OpenCPU website
    has detailed documentation and example apps.
	"""
	
	homepage = "https://www.opencpu.org"
	cran = "opencpu" 

	version("2.2.11", md5="24b7991213fd80293dbd775721ee3bb7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-evaluate@0.12:", type=("build", "run"))
	depends_on("r-httpuv@1.3:", type=("build", "run"))
	depends_on("r-knitr@1.6:", type=("build", "run"))
	depends_on("r-jsonlite@1.4:", type=("build", "run"))
	depends_on("r-remotes@2.0.2:", type=("build", "run"))
	depends_on("r-sys@2.1:", type=("build", "run"))
	depends_on("r-webutils@0.6:", type=("build", "run"))
	depends_on("r-curl@4:", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-protolite", type=("build", "run"))
	depends_on("r-brew", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
