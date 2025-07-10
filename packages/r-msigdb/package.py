# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsigdb(RPackage):
	"""An ExperimentHub Package for the Molecular Signatures Database (MSigDB)

	This package provides the Molecular Signatures Database (MSigDB) in a R accessible objects. Signatures are stored in GeneSet class objects form the GSEABase package and the entire database is stored in a GeneSetCollection object. These data are then hosted on the ExperimentHub. Data used in this package was obtained from the MSigDB of the Broad Institute. Metadata for each gene set is stored along with the gene set in the GeneSet class object.
	"""
	
	homepage = "https://davislaboratory.github.io/msigdb"
	bioc = "msigdb" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/msigdb_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/msigdb/msigdb_1.10.0.tar.gz"]

	version("1.10.0", sha256="3a2a26d1a63fc22fba2f99849957c201fd98ade32e0f6f27853f1560c3c0efbb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

