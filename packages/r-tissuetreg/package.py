# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTissuetreg(RPackage):
	"""TWGBS and RNA-seq data from tissue T regulatory cells from mice

	The package provides ready to use epigenomes (obtained from TWGBS) and transcriptomes (RNA-seq) from various tissues as obtained in the study (Delacher and Imbusch 2017, PMID: 28783152). Regulatory T cells (Treg cells) perform two distinct functions: they maintain self-tolerance, and they support organ homeostasis by differentiating into specialized tissue Treg cells. The underlying dataset characterises the epigenetic and transcriptomic modifications for specialized tissue Treg cells.
	"""
	
	homepage = "https://github.com/cimbusch/tissueTreg"
	bioc = "tissueTreg"

	version("1.28.0", commit="290bbb85cb806353cca63f85bc0a9ae1acba9eb4")
	version("1.22.0", commit="6b37bb058d93c8de73255d8b2845d5e12ed488fd")

	depends_on("r@3.5:", type=("build", "run"))

