# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAnnotatedTypes(PythonPackage):
    """Reusable constraint types to use with typing.Annotated"""
    
    homepage = "https://github.com/annotated-types/annotated-types"
    pypi = "annotated-types/annotated_types-0.7.0-py3-none-any.whl" 

    version("0.1.0", sha256="950981439bbaba02482f5d7c68c6de529c19eb8f321896c60d6debcda5e2a747", expand=False, url="https://files.pythonhosted.org/packages/e8/36/4eb8221e09a75ecde013080851d5e90d7ea2b605a3a1b9d9f154831e5ca2/annotated_types-0.1.0-py3-none-any.whl")
    version("0.2.0", sha256="5e7d2e6f477b7abe7b44c1903bb5fb86320fa2fa41837d8e9a81c7beb999a079", expand=False, url="https://files.pythonhosted.org/packages/1d/3f/bd2fb1eb48062ee269d8c9692bb1c900d14f781ea760e40d7fadb4698265/annotated_types-0.2.0-py3-none-any.whl")
    version("0.3.0", sha256="229951d843ef3877d2bddcb1aa22990868eef22cf8e88140eacee803b83e09a4", expand=False, url="https://files.pythonhosted.org/packages/6e/6d/c91d549204fb4413c95b7f1366b6ceb7afa5e0f796be3459e94dbaa92e78/annotated_types-0.3.0-py3-none-any.whl")
    version("0.3.1", sha256="de6be29714cc5943221d5fc75cfa2293d78b2ad99ef6dc4d46abe59522b742f3", expand=False, url="https://files.pythonhosted.org/packages/0c/4f/416437e08635edb6116c707d38fff5ae361b5887e75fb213ed057ce6cf4e/annotated_types-0.3.1-py3-none-any.whl")
    version("0.4.0", sha256="ac27bcccc7a1447efe9a9bd1145766cc14a841b107a6040a799c260e83adf67d", expand=False, url="https://files.pythonhosted.org/packages/72/06/228244d7bc5db85719963cb957abd097ecc0e412053c70a4d3d5ef7cd5f3/annotated_types-0.4.0-py3-none-any.whl")
    version("0.5.0", sha256="58da39888f92c276ad970249761ebea80ba544b77acddaa1a4d6cf78287d45fd", expand=False, url="https://files.pythonhosted.org/packages/d8/f0/a2ee543a96cc624c35a9086f39b1ed2aa403c6d355dfe47a11ee5c64a164/annotated_types-0.5.0-py3-none-any.whl")
    version("0.6.0", sha256="0641064de18ba7a25dee8f96403ebc39113d0cb953a01429249d5c7564666a43", expand=False, url="https://files.pythonhosted.org/packages/28/78/d31230046e58c207284c6b2c4e8d96e6d3cb4e52354721b944d3e1ee4aa5/annotated_types-0.6.0-py3-none-any.whl")
    version("0.7.0", sha256="1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", expand=False, url="https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.8:", type=("build", "run"))

# {'typing-extensions(>=4.0.0,<5.0.0);python_full_version<"3.9.0"': ['0.2.0', '0.3.0', '0.3.1'], "typing-extensions>=4.0.0;python_version<'3.9'": ['0.4.0', '0.5.0', '0.6.0', '0.7.0']}