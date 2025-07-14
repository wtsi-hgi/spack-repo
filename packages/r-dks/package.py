# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDks(RPackage):
	"""The double Kolmogorov-Smirnov package for evaluating multiple testing procedures.

	The dks package consists of a set of diagnostic functions for multiple testing methods. The functions can be used to determine if the p-values produced by a multiple testing procedure are correct. These functions are designed to be applied to simulated data. The functions require the entire set of p-values from multiple simulated studies, so that the joint distribution can be evaluated.
	"""
	
	bioc = "dks" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/dks_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/dks/dks_1.48.0.tar.gz"]

    version("1.54.0", tag="RELEASE_3_21")
	version("1.48.0", sha256="4d07b926a96f30329cb9fbd324425f678e651d725dadcff36782812fd7d95c77")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
