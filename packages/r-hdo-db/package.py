# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdoDb(RPackage):
	"""A set of annotation maps describing the entire Human Disease Ontology.

	A set of annotation maps describing the entire Human Disease Ontology
	assembled using data from DO.  Its annotation data comes from
	https://github.com/DiseaseOntology/HumanDiseaseOntology/tree/main/src/ontology."""
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/HDO.db_0.99.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/HDO.db/HDO.db_0.99.1.tar.gz"]
	bioc = "HDO.db"
	version("0.99.1", md5="007a50523f1de27048dfc97f4d458f59")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation