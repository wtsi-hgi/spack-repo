# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnshuman(RPackage):
	"""Human Gene Annotation Data from 'Ensembl'

	Gene information from 'Ensembl' genome builds 'GRCh38.p14' and 'GRCh37.p13' to use with the 'topr' package. The datasets were originally downloaded from <https://ftp.ensembl.org/pub/current/gtf/homo_sapiens/Homo_sapiens.GRCh38.111.gtf.gz> and <https://ftp.ensembl.org/pub/grch37/current/gtf/homo_sapiens/Homo_sapiens.GRCh37.87.gtf.gz> and converted into the format required by the 'topr' package. See <https://github.com/totajuliusd/topr?tab=readme-ov-file#how-to-use-topr-with-other-species-than-human> to see the required format.
	"""
	
	cran = "enshuman" 

	version("1.0.0", md5="af72d84840c3a1a0ef7cd852852e9d16")

	depends_on("r@3.5:", type=("build", "run"))
