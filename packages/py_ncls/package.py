# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNcls(PythonPackage):
    """A fast interval tree-like implementation in C, wrapped for the Python ecosystem.
    
    The Nested Containment List is a datastructure for interval overlap queries, like the interval tree. It is usually an order of magnitude faster than the interval tree both for building and query lookups.
    The implementation here is a revived version of the one used in the now defunct PyGr library, which died of bitrot. I have made it less memory-consuming and created wrapper functions which allows batch-querying the NCLS for further speed gains.
    It was implemented to be the cornerstone of the PyRanges project, but I have made it available to the Python community as a stand-alone library. Enjoy.
    """    

    homepage = "https://github.com/pyranges/ncls"
    pypi = "ncls/ncls-0.0.68.tar.gz"

    version("0.0.68", sha256="81aaa5abb123bb21797ed2f8ef921e20222db14a3ecbc61ccf447532f2b7ba93")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cython")

