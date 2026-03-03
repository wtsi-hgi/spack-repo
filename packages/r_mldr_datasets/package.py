# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMldrDatasets(RPackage):
	"""R Ultimate Multilabel Dataset Repository

	Large collection of multilabel datasets along with the functions
    needed to export them to several formats, to make partitions, and to obtain
    bibliographic information.
	"""
	
	homepage = "https://github.com/fcharte/mldr.datasets"
	cran = "mldr.datasets" 

	version("0.4.2", md5="6bc68fd7b353d6fa9f33b377d75a6409")

	depends_on("r@3:", type=("build", "run"))
