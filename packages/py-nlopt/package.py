# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyNlopt(PythonPackage):
    """Library for nonlinear optimization, wrapping many algorithms for global and local, constrained or unconstrained, optimization"""
    
    homepage = "None"
    pypi = "nlopt/nlopt-2.9.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl" 

    version("2.4.2.post1", sha256="cf8c05e08c68ce57ad7082deaa8fe14c8b97c99c4b5810cd62f3046e3734b2e7")
    version("2.4.2.post2", sha256="841559c827f0b2d42ba8fbf2e3864f2b5584f45c0434bce73a358e5e588f0cf0")
    version("2.6.1", sha256="38d7ad534dc9802f53ff7e36967ba44969cddd66d19ebe2a13ede84c560e6be6", expand=False, url="https://files.pythonhosted.org/packages/03/4a/a7375732d74dca7d2d564e88be8976bd3ba50474bd9bb155dd8fc71d0639/nlopt-2.6.1-py3-none-manylinux1_x86_64.whl")
    version("2.6.2-py36", sha256="6c76d6cdb2d523b56927ddc6bd43e4f04a52812d2b28c2f0a04e9689f4c52139", expand=False, url="https://files.pythonhosted.org/packages/c6/f5/526390f2115bf522b8337a928e02897fd694ca2dd25ff521ce49cc50a52a/nlopt-2.6.2-cp36-cp36m-manylinux2010_x86_64.whl")
    version("2.6.2-py37", sha256="1f34e8b007b94bbc452b89faea6272f58ab77f75d0aee9f1b01db68fc7729e74", expand=False, url="https://files.pythonhosted.org/packages/0a/da/aeccfaf0b772cb87c4932d13ee5d741a86dc225e773b28206bb2bd2f7c3c/nlopt-2.6.2-cp37-cp37m-manylinux2010_x86_64.whl")
    version("2.6.2-py38", sha256="5ebdd6870d842b83333704459fa3490fc1fd1c167a9854978f3e96e14af77940", expand=False, url="https://files.pythonhosted.org/packages/a2/bc/0690f6b9b74eb615b8c305859bcaedce13bdda9f6c313fd5ab3e982b4b66/nlopt-2.6.2-cp38-cp38-manylinux2010_x86_64.whl")
    version("2.7.0-py36", sha256="93664756aa571fa4a875f2feddc9594f5daf5432d58222879b70a79c6dcdb522", expand=False, url="https://files.pythonhosted.org/packages/a7/34/2b2bfd86b8f337ddfe332117a6657e43dd93aba161ceee7b98db9b91d7b0/nlopt-2.7.0-cp36-cp36m-manylinux2014_x86_64.whl")
    version("2.7.0-py37", sha256="c8e38964a8f69444e4456cddd81e9d3c1e8d6b2089f7c70ddad5fe6a7003daf9", expand=False, url="https://files.pythonhosted.org/packages/a6/e3/c31eb64ab24c367641a76c88f0e09dbea3e6210e5371da2c452d2721eaef/nlopt-2.7.0-cp37-cp37m-manylinux2014_x86_64.whl")
    version("2.7.0-py38", sha256="dd41c54d2016acf937bc7a40d30288d87c9f337e4c6ef99f04b023c9ffda1142", expand=False, url="https://files.pythonhosted.org/packages/c7/7d/b9ab52ab89301235d30d9ac1b9f0234f64246c3d0149dd2fbe866a4f01b1/nlopt-2.7.0-cp38-cp38-manylinux2014_x86_64.whl")
    version("2.7.0-py39", sha256="49e6ed686e7e2ee7747f9c6498823462dbf09b46b4f54f2842a4b938cd772d98", expand=False, url="https://files.pythonhosted.org/packages/ef/07/8fefcfca9fa757784620f9185bc316edd82a551e95d6459634029fdd44ad/nlopt-2.7.0-cp39-cp39-manylinux2014_x86_64.whl")
    version("2.7.1-py310", sha256="6ba0862162248442fbf1f04b20a321c11ff40ff4442a12aaaafcdaff9abb0ab7", expand=False, url="https://files.pythonhosted.org/packages/ac/7a/78301ab01e31e08bc850bf800f34133c823579ace029d7898afe94745571/nlopt-2.7.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.7.1-py311", sha256="3e1653de0060a42d6709423e6160888893bb688f4ff79aa0f1def4701ea25dd8", expand=False, url="https://files.pythonhosted.org/packages/54/4e/a7123adf391ed71175c5c8e8217be2ac3c335cb67c3601d183e94337393d/nlopt-2.7.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.7.1-py312", sha256="592ded3b34bb888cd99c5da3fb1c3c9269ddd996dade578a8ec325cd8b6be752", expand=False, url="https://files.pythonhosted.org/packages/7d/5c/f2f676df69694b774df64ec6725cff1f43b5b4d43a421339cac865731906/nlopt-2.7.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.7.1-py37", sha256="aad38bab99348f6c3bbf0d5f339b3fd77465b27ef44c330f4ba512a40b87b373", expand=False, url="https://files.pythonhosted.org/packages/18/53/3e6f01d28488dc335a4f67ec3487d6c565b015a0036b7fee3b5412c6814f/nlopt-2.7.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.7.1-py38", sha256="33f9370bd37788b4ac792cf161835f1e4e9bbad8bfb5a76f75a295ae38dcd8d0", expand=False, url="https://files.pythonhosted.org/packages/5b/77/aee1257d3f54b6c24dd6e59c8eeb52a347190942a7aed9ebe4e296e565fd/nlopt-2.7.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.7.1-py39", sha256="b4a05448f0ffebbab7a6a822297430e018c848652280e6efa13484e210291d5c", expand=False, url="https://files.pythonhosted.org/packages/43/d1/d8b639cb1e40472d29567280f105cdaf1517cf8fdfa226303b6d46f5968d/nlopt-2.7.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.8.0-py310", sha256="893409b0321353c60945b270e549ec364665bb38c66f989df7bbe32c50886dd8", expand=False, url="https://files.pythonhosted.org/packages/89/fc/0b3d0fa9801d876dfc59dea173645e0084b39a89cfa9ca90da3a2915ac54/nlopt-2.8.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.8.0-py311", sha256="b8631dcf532219156217c1c3b04ec1dea22a7368ec0d5ce958a93717acca82ca", expand=False, url="https://files.pythonhosted.org/packages/ad/7b/2f264a48659facb61f7d983b7a9b6c2feca1cdf3aac38317df00b7b960d9/nlopt-2.8.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.8.0-py312", sha256="2fac548c26f2837f348f204860ba2ba49c60bddfe1d280e11f9a0c66dde4b1c9", expand=False, url="https://files.pythonhosted.org/packages/9c/41/eb8e9aaa74998c3d35de0efafdaf76812739d366635efb7e46fd2c0e668a/nlopt-2.8.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.8.0-py313", sha256="fc2f065ca5f6b25c4f160468f1fc6272795267fb3b3d9ff4809a8a34e0b6da98", expand=False, url="https://files.pythonhosted.org/packages/91/5c/dd2ef32b609e39c1e7058153567dc269623f36644c09d3840ee11a418050/nlopt-2.8.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.8.0-py39", sha256="8eaced0601a2bbeca61bd9ecd1e58ccada15fbd4a89d81b38c8659504875e1b2", expand=False, url="https://files.pythonhosted.org/packages/92/ef/6a6a0a4f5f04fb0329072ad328753dd85da5e26dfd49bac76ffbd88fa6b6/nlopt-2.8.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.9.0-py310", sha256="422bac893488fa54b961f70486e9a553f10c6aaf71f27d3f64e9c48de4b33ba7", expand=False, url="https://files.pythonhosted.org/packages/36/3f/60647fbdd9f57c4be383f61cbb6b0df3bd45cba465a32e1ed434d1bb0062/nlopt-2.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.9.0-py311", sha256="bcb9e04bcd91e694a893d09dd7c71421c024d499d5c15275f5f8cf54d594776c", expand=False, url="https://files.pythonhosted.org/packages/04/71/77ddd19a88f6a598f47aa3291190971f8be8eb4891ba0220ecfb2ddc55f5/nlopt-2.9.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.9.0-py312", sha256="cfb42c90e6005521481696ce0ee08070e295d7046e5d810c5e0871dd5f82431c", expand=False, url="https://files.pythonhosted.org/packages/e8/ce/1b208e71fba9d81e5f45250d1ff19f1fda5aeb74cab2ccc09303296f4aec/nlopt-2.9.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.9.0-py313", sha256="4c642538ec7698be12036c9bb0dbc0a50f6aa31e3790f67ac96aabf01306c5c3", expand=False, url="https://files.pythonhosted.org/packages/45/5a/913eae06b3140cefb9ba9a2632ebebf77114e728e5a7139c4a1668811dac/nlopt-2.9.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.9.0-py39", sha256="cf9576f7bfd779212219a3879d3c1d19a2390b7cab51d6b2b5fe1ffc2e5cf576", expand=False, url="https://files.pythonhosted.org/packages/f8/32/44b18844f448fb9408fba051ca081f0d5cc447aa338320306de64811c391/nlopt-2.9.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.9.1-py310", sha256="ad7b5f3553a1ff5b1e762a3c813cea57f644fa91ad50f0def3e7f184860daa0e", expand=False, url="https://files.pythonhosted.org/packages/54/b5/65f5c18e7b0b6e04960aa42003994ece0ff22752731de61a5db52bac2499/nlopt-2.9.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.9.1-py311", sha256="597bbaed7f0a3b20f8942c545e504bba421628cce393c17c6cfe3c9a9ed4266a", expand=False, url="https://files.pythonhosted.org/packages/78/3b/31d5fb489cece11c274d52f4dcacd8e462738a4f2a584061d06d6a1d5f80/nlopt-2.9.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.9.1-py312", sha256="bf1d0b8c0047accffe69613450c17049d67474bd9fdd6213d849bd1e92b83aba", expand=False, url="https://files.pythonhosted.org/packages/ee/2f/e2089a355718885a2310bd86ab54c3dbf3d83165b825621f49ad63b4ed39/nlopt-2.9.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.9.1-py313", sha256="80bfa95aa80d7cea9b30ac304daba17ce8b00f25f7ed37bbe28a074d1892b168", expand=False, url="https://files.pythonhosted.org/packages/f0/28/fc6e4fbe4d689e78deca171540fbc0993ac1a9ac797a284f2b2e73289311/nlopt-2.9.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("2.9.1-py39", sha256="2098cf6e3fa65d35b9fc6455f9cb7711af351a9811155280a3732fcf153bc299", expand=False, url="https://files.pythonhosted.org/packages/85/f7/b9df697e466aebf557362f4ad8f3f363447e679c5f66cb6bcc596ea2e888/nlopt-2.9.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-numpy@1.18.5:", type=("build", "run"))
    depends_on("python@3.6", when="@2.6.2-py36", type=("build", "run"))
    depends_on("python@3.7", when="@2.6.2-py37", type=("build", "run"))
    depends_on("python@3.8", when="@2.6.2-py38", type=("build", "run"))
    depends_on("python@3.6", when="@2.7.0-py36", type=("build", "run"))
    depends_on("python@3.7", when="@2.7.0-py37", type=("build", "run"))
    depends_on("python@3.8", when="@2.7.0-py38", type=("build", "run"))
    depends_on("python@3.9", when="@2.7.0-py39", type=("build", "run"))
    depends_on("python@3.10", when="@2.7.1-py310", type=("build", "run"))
    depends_on("python@3.11", when="@2.7.1-py311", type=("build", "run"))
    depends_on("python@3.12", when="@2.7.1-py312", type=("build", "run"))
    depends_on("python@3.7", when="@2.7.1-py37", type=("build", "run"))
    depends_on("python@3.8", when="@2.7.1-py38", type=("build", "run"))
    depends_on("python@3.9", when="@2.7.1-py39", type=("build", "run"))
    depends_on("python@3.10", when="@2.8.0-py310", type=("build", "run"))
    depends_on("python@3.11", when="@2.8.0-py311", type=("build", "run"))
    depends_on("python@3.12", when="@2.8.0-py312", type=("build", "run"))
    depends_on("python@3.13", when="@2.8.0-py313", type=("build", "run"))
    depends_on("python@3.9", when="@2.8.0-py39", type=("build", "run"))
    depends_on("python@3.10", when="@2.9.0-py310", type=("build", "run"))
    depends_on("python@3.11", when="@2.9.0-py311", type=("build", "run"))
    depends_on("python@3.12", when="@2.9.0-py312", type=("build", "run"))
    depends_on("python@3.13", when="@2.9.0-py313", type=("build", "run"))
    depends_on("python@3.9", when="@2.9.0-py39", type=("build", "run"))
    depends_on("python@3.10", when="@2.9.1-py310", type=("build", "run"))
    depends_on("python@3.11", when="@2.9.1-py311", type=("build", "run"))
    depends_on("python@3.12", when="@2.9.1-py312", type=("build", "run"))
    depends_on("python@3.13", when="@2.9.1-py313", type=("build", "run"))
    depends_on("python@3.9", when="@2.9.1-py39", type=("build", "run"))

# {'numpy(>=1.14)': ['2.6.1', '2.6.2-py36', '2.6.2-py37', '2.6.2-py38', '2.7.0-py36', '2.7.0-py37', '2.7.0-py38', '2.7.0-py39', '2.7.1-py310', '2.7.1-py37', '2.7.1-py38', '2.7.1-py39'], 'numpy(>=1.18.5)': ['2.7.1-py311'], 'numpy>=1.18.5': ['2.7.1-py312'], 'numpy<3,>=2': ['2.8.0-py310', '2.8.0-py311', '2.8.0-py312', '2.8.0-py313', '2.8.0-py39', '2.9.0-py310', '2.9.0-py311', '2.9.0-py312', '2.9.0-py313', '2.9.0-py39', '2.9.1-py310', '2.9.1-py311', '2.9.1-py312', '2.9.1-py313', '2.9.1-py39']}