# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBibliorefer(RPackage):
	"""Generator of Main Scientific References

	Generates a list, with a size defined by the user, containing the main scientific references and the frequency distribution of authors and journals in the list obtained.
    The database is a dataframe with academic production metadata made available by bibliographic collections such as Scopus, Web of Science, etc.
    The temporal evolution of scientific production on a given topic is presented and ordered lists of articles are constructed by number of citations and of authors and journals by level of productivity.
    Massimo Aria, Corrado Cuccurullo. (2017) <doi:10.1016/j.joi.2017.08.007>.
    Caibo Zhou, Wenyan Song. (2021) <doi:10.1016/j.jclepro.2021.126943>.
	"""
	
	cran = "bibliorefer" 

	version("0.1.0", md5="acb1251d0c8273ac43ca31a64323ce4c")

	depends_on("r@2.10:", type=("build", "run"))
