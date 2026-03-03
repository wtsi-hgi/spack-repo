# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyn(RPackage):
	"""Creates Synonyms From Target Words

	Generates synonyms from a given word drawing from a synonym list
    from the 'moby' project <http://moby-thesaurus.org/>.
	"""
	
	homepage = "http://syn.njtierney.com/"
	cran = "syn" 

	version("0.1.0", md5="d627b8ad5d7d710b89895ce71f145b9d")

	depends_on("r@3.4:", type=("build", "run"))
