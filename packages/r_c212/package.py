# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RC212(RPackage):
	"""Methods for Detecting Safety Signals in Clinical Trials Using
Body-Systems (System Organ Classes)

	Methods for detecting safety signals in clinical trials using groupings of adverse events by body-system or system organ class. This work was supported by the Engineering and Physical Sciences Research Council (UK) (EPSRC) [award reference 1521741] and Frontier Science (Scotland) Ltd. The package title c212 is in reference to the original Engineering and Physical Sciences Research Council (UK) funded project which was named CASE 2/12.
	"""
	
	cran = "c212" 

	version("0.98", md5="6e88f0d0d4bafb6b970634feb6bbbdb7", url="https://cran.r-project.org/src/contrib/c212_0.98.tar.gz")

	depends_on("r-coda", type=("build", "run"))
