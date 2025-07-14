# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpoDb(RPackage):
	"""A set of annotation maps describing the Mouse Phenotype Ontology

	We have developed the human disease ontology R package HDO.db, which provides the semantic relationship between human diseases. Relying on the DOSE and GOSemSim packages we developed, we can carry out disease enrichment and semantic similarity analyses. Many biological studies are achieved through mouse models, and a large number of data indicate the association between genotypes and phenotypes or diseases.  The study of model organisms can be transformed into useful knowledge about normal human biology and disease to facilitate treatment and early screening for diseases. Organism-specific genotype-phenotypic associations can be applied to cross-species phenotypic studies to clarify previously unknown phenotypic connections in other species. Using the same principle to diseases can identify genetic associations and even help to identify disease associations that are not obvious. Therefore, as a supplement to HDO.db and DOSE, we developed mouse phenotypic ontology R package MPO.db.
	"""
	
	homepage = "https://github.com/YuLab-SMU/MPO.db"
	bioc = "MPO.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/MPO.db_0.99.7.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/MPO.db/MPO.db_0.99.7.tar.gz"]

    version("0.99.8", tag="RELEASE_3_21")
	version("0.99.7", sha256="74b3e8f0a3b5b896b5d0c944e3334c750a4404b800fa70da9a2aa1f066643974")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))

