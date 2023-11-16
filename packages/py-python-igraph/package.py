# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyPythonIgraph(PythonPackage):
    """
    High performance graph data structures and algorithms (legacy package)
    """
    homepage = "https://igraph.org/python"
    pypi     = "python-igraph/python-igraph-0.11.2.tar.gz"
    
    version('0.11.2', sha256='ab2e3497b92944f9036e419e9b731bde803fa649fbf0e53cf19bc7e51ac7db3e')

    depends_on("py-setuptools", type="build")
