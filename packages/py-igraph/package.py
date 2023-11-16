# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

class PyIgraph(PythonPackage):
    """
    High performance graph data structures and algorithms
    """

    homepage = "https://igraph.org/python"
    pypi     = "igraph/igraph-0.11.2.tar.gz"
    

    version("0.11.2", sha256="c4053e47156d7685ad48bd72e6ff400d46b09deeebc746b96b5cf9737939fa2d")

    depends_on("py-setuptools", type="build")
    depends_on("cmake")
