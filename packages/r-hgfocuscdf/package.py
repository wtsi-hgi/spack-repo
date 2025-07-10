# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgfocuscdf(RPackage):
	"""hgfocuscdf

	A package containing an environment representing the HG-Focus.CDF file.
	"""
	
	bioc = "hgfocuscdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgfocuscdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgfocuscdf/hgfocuscdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="ca1f4370b5c748f619906df649ffeae92b718f1ea021a5efc79838c9f9f8af6f")

	depends_on("r-annotationdbi", type=("build", "run"))

