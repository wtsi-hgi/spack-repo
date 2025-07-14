# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcoil(RPackage):
	"""Prediction of Oligomerization of Coiled Coil Proteins

	The package allows for predicting whether a coiled coil sequence (amino acid sequence plus heptad register) is more likely to form a dimer or more likely to form a trimer. Additionally to the prediction itself, a prediction profile is computed which allows for determining the strengths to which the individual residues are indicative for either class. Prediction profiles can also be visualized as curves or heatmaps.
	"""
	
	homepage = "http://www.bioinf.jku.at/software/procoil/"
	bioc = "procoil" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/procoil_2.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/procoil/procoil_2.30.0.tar.gz"]

    version("2.36.0", tag="RELEASE_3_21")
	version("2.30.0", sha256="c12e4cddd0bf40648d0bc19b94e8fc7c22d6753e8deebdca62630ca9c7901a08")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-kebabs", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
