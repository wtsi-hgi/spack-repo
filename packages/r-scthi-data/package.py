# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScthiData(RPackage):
	"""The package contains examples of single cell data used in vignettes and examples of the scTHI package; data contain both tumor cells and immune cells from public dataset of glioma

	Data for the vignette and tutorial of the package scTHI.
	"""
	
	bioc = "scTHI.data" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/scTHI.data_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/scTHI.data/scTHI.data_1.14.0.tar.gz"]

    version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="88f0ad5cbcc14775be616a9ab2a08fd2a5ff6893d53f48ee4a9676c11be548f8")

	depends_on("r@4:", type=("build", "run"))

