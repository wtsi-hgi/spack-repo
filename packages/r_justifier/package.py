# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJustifier(RPackage):
	"""Human and Machine-Readable Justifications and Justified
Decisions Based on 'YAML'

	Leverages the 'yum' package to
             implement a 'YAML' ('YAML Ain't Markup Language', a human
             friendly standard for data serialization; see <https:yaml.org>)
             standard for documenting justifications, such as for decisions
             taken during the planning, execution and analysis of a study
             or during the development of a behavior change intervention
             as illustrated by Marques & Peters (2019)
             <doi:10.17605/osf.io/ndxha>. These justifications are both
             human- and machine-readable, facilitating efficient extraction
             and organisation.
	"""
	
	homepage = "https://r-packages.gitlab.io/justifier"
	cran = "justifier" 

	version("0.2.6", md5="9754dd65a909dde6d4524a7a1d593894")

	depends_on("r-data-tree@0.7.8:", type=("build", "run"))
	depends_on("r-diagrammer@1:", type=("build", "run"))
	depends_on("r-diagrammersvg@0.1:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-yaml@2.2:", type=("build", "run"))
	depends_on("r-yum@0.0.1:", type=("build", "run"))
