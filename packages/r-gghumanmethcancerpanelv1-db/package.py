# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGghumanmethcancerpanelv1Db(RPackage):
	"""Illumina Golden Gate Human Methylation Cancer Panel Version 1 annotation data (chip GGHumanMethCancerPanelv1)

	Illumina Golden Gate Human Methylation Cancer Panel Version 1 annotation data (chip GGHumanMethCancerPanelv1) assembled using data from public repositories
	"""
	
	bioc = "GGHumanMethCancerPanelv1.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/GGHumanMethCancerPanelv1.db_1.4.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/GGHumanMethCancerPanelv1.db/GGHumanMethCancerPanelv1.db_1.4.1.tar.gz"]

	version("1.4.1", md5="e8f4a37182b175fb33dd54f8093e6f52")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@2.4.5:", type=("build", "run"))
	depends_on("r-annotationforge", type=("build", "run"))

