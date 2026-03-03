# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrimpute(RPackage):
	"""Imputing Dropout Events in Single-Cell RNA-Sequencing Data

	R codes for imputing dropout events. Many statistical methods in cell type identification, visualization and lineage reconstruction do not account for dropout events ('PCAreduce', 'SC3', 'PCA', 't-SNE', 'Monocle', 'TSCAN', etc). 'DrImpute' can improve the performance of such software by imputing dropout events.
	"""
	
	homepage = "https://github.com/ikwak2/DrImpute"
	cran = "DrImpute" 

	version("1.0", md5="37c40d0791ff3c6cc328893c5d2f19e2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
