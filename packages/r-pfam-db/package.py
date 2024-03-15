# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPfamDb(RPackage):
	"""A set of protein ID mappings for PFAM.

	A set of protein ID mappings for PFAM assembled using data from
	public repositories."""

	bioc = "PFAM.db"
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/PFAM.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/PFAM.db/PFAM.db_3.18.0.tar.gz"]

	version("3.18.0", md5="f98f5d1e5d335e6bbf1ea6426cde67bb")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation