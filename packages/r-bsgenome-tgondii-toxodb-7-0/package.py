# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeTgondiiToxodb70(RPackage):
	"""Toxoplasma gondii ME49 (ToxoDB-7.0)

	Toxoplasma gondii ME49 genome Release 7.0 available at http://www.toxodb.org
	"""
	
	bioc = "BSgenome.Tgondii.ToxoDB.7.0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Tgondii.ToxoDB.7.0_0.99.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Tgondii.ToxoDB.7.0/BSgenome.Tgondii.ToxoDB.7.0_0.99.1.tar.gz"]

	version("0.99.1", md5="f67644d1a897fe2ff4139832d4ceaf80", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Tgondii.ToxoDB.7.0_0.99.1.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

