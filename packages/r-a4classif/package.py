# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RA4classif(RPackage):
	"""Automated Affymetrix Array Analysis Classification Package.

	Functionalities for classification of Affymetrix microarray data,
	integrating within the Automated Affymetrix Array Analysis set of
	packages."""

	bioc = "a4Classif"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/a4Classif_1.50.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/a4Classif/a4Classif_1.50.0.tar.gz"]

	version("1.50.0", md5="2af82160c9909dd6fdec620de5710cfa")

	depends_on("r-a4core", type=("build", "run"))
	depends_on("r-a4preproc", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-pamr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-varselrf", type=("build", "run"))
