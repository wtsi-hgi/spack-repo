# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcolicdf(RPackage):
	"""ecolicdf

	A package containing an environment representing the Ecoli.CDF file.
	"""
	
	bioc = "ecolicdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ecolicdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ecolicdf/ecolicdf_2.18.0.tar.gz"]

	version("2.18.0", md5="4e664c1ac41a8ab68ef22f8a889b916c")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation