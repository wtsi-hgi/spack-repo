# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTmtoolkit(PythonPackage):
    """tmtoolkit is a set of tools for text mining and topic modeling with Python developed especially for the use in the social sciences, linguistics, journalism or related disciplines. It aims for easy installation, extensive documentation and a clear programming interface while offering good performance on large datasets by the means of vectorized operations (via NumPy) and parallel computation (using Python's multiprocessing module and the loky package). The basis of tmtoolkit's text mining capabilities are built around SpaCy, which offers many language models."""

    homepage = "https://github.com/internaut/tmtoolkit"
    pypi = "tmtoolkit/tmtoolkit-0.12.0.tar.gz"

    version("0.12.0", sha256="6df5429cd675989f21d9f075ddb11fe5ae273d6544fc337a2589bab2bc331909")
