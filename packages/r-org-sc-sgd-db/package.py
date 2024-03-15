# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgScSgdDb(RPackage):
	"""Genome wide annotation for Yeast

	Genome wide annotation for Yeast, primarily based on mapping using ORF identifiers from SGD.
	"""
	
	bioc = "org.Sc.sgd.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Sc.sgd.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Sc.sgd.db/org.Sc.sgd.db_3.18.0.tar.gz"]

	version("3.18.0", md5="cd83de7109be623e7a294a47ca65f160")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation