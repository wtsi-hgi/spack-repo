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

    version("0.99.8", commit="653dfe088df4ac66d6f56d751a485b0c4edcf70c")
    version("0.99.7", commit="76f7a15a7a3de6f43bec30588cbc17b769c7d30b")

    depends_on("r@4.3:", type=("build", "run"))
    # Ensure a recent Bioconductor snapshot so required AnnotationHub
    # resources (added 2024-08-01) are available during install/load
    depends_on("r-biocversion@3.21:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
