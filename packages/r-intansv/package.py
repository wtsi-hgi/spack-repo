# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntansv(RPackage):
	"""Integrative analysis of structural variations

	This package provides efficient tools to read and integrate structural variations predicted by popular softwares. Annotation and visulation of structural variations are also implemented in the package.
	"""
	
	bioc = "intansv" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/intansv_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/intansv/intansv_1.42.0.tar.gz"]

    version("1.48.0", tag="RELEASE_3_21")
	version("1.42.0", sha256="e13c11ea33934d497c7b47f6c3cd344b6d894c4cd73a55f0b6f7ae28ef13a444")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggbio", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
