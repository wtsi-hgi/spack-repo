# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirna102xgaincdf(RPackage):
	"""mirna102xgaincdf

	A package containing an environment representing the miRNA-1_0_2Xgain.CDF file.
	"""
	
	bioc = "mirna102xgaincdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mirna102xgaincdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mirna102xgaincdf/mirna102xgaincdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="f1845972e5781e4ee47b65faa9e87d8e376c2fe8efbe55e48ef48265700b070f")

	depends_on("r-annotationdbi", type=("build", "run"))

