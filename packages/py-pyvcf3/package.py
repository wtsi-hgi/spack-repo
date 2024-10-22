# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyvcf3(PythonPackage):
    """The intent of this module is to mimic the csv module in the Python stdlib, as opposed to more flexible serialization formats like JSON or YAML. vcf will attempt to parse the content of each record based on the data types specified in the meta-information lines -- specifically the ##INFO and ##FORMAT lines. If these lines are missing or incomplete, it will check against the reserved types mentioned in the spec. Failing that, it will just return strings."""

    homepage = "https://github.com/dridk/PyVCF3"
    pypi = "PyVCF3/PyVCF3-1.0.3.tar.gz"

    version("1.0.3", sha256="4b16d71c8b97010487e2c939fb4d5707b7bbfa4e2b313df9dba3e372c5ba031d")

    depends_on("py-setuptools", type="build")
