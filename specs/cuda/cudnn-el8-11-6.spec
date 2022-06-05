%global __os_install_post %{nil}

Name:           cudnn-11-6
Version:        8.4.0.27
Release:        2
Summary:        CUDA Deep Neural Network library

License:        NVIDIA Proprietary
Group:          Unspecified
URL:            https://developer.nvidia.com
Source0:        cudnn-linux-x86_64-8.4.0.27_cuda11.6-archive.tar.gz

Vendor:         Nvidia
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
BuildArch:      x86_64
Requires:       cuda-11-6 >= 11.6.2
Prefix:         /usr/local/cuda-11.6
Prefix:         /usr/lib64/pkgconfig

%description
The NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated library
of primitives for deep neural networks. cuDNN provides highly tuned
implementations for standard routines such as forward and backward convolution,
pooling, normalization, and activation layers. cuDNN is part of the NVIDIA Deep
Learning SDK.

This RPM was packaged for Rocky Linux 8 with libraries built against CUDA 11.6.

%prep
%setup -q -n cudnn-linux-x86_64-8.4.0.27_cuda11.6-archive
%{__rm} -f lib/libcudnn_adv_infer.so
%{__rm} -f lib/libcudnn_adv_infer.so.8
%{__rm} -f lib/libcudnn_adv_infer_static_v8.a
%{__rm} -f lib/libcudnn_adv_train.so
%{__rm} -f lib/libcudnn_adv_train.so.8
%{__rm} -f lib/libcudnn_adv_train_static_v8.a
%{__rm} -f lib/libcudnn_cnn_infer.so
%{__rm} -f lib/libcudnn_cnn_infer.so.8
%{__rm} -f lib/libcudnn_cnn_infer_static_v8.a
%{__rm} -f lib/libcudnn_cnn_train.so
%{__rm} -f lib/libcudnn_cnn_train.so.8
%{__rm} -f lib/libcudnn_cnn_train_static_v8.a
%{__rm} -f lib/libcudnn_ops_infer.so
%{__rm} -f lib/libcudnn_ops_infer.so.8
%{__rm} -f lib/libcudnn_ops_infer_static_v8.a
%{__rm} -f lib/libcudnn_ops_train.so
%{__rm} -f lib/libcudnn_ops_train.so.8
%{__rm} -f lib/libcudnn_ops_train_static_v8.a
%{__rm} -f lib/libcudnn.so
%{__rm} -f lib/libcudnn.so.8

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_prefix}/local/cuda-11.6
%{__mkdir} -p %{buildroot}%{_prefix}/local/cuda-11.6/lib64
%{__mkdir} -p %{buildroot}%{_prefix}/local/cuda-11.6/include
%{__install} -m 644 LICENSE %{buildroot}%{_prefix}/local/cuda-11.6/cuDNN-LICENSE
%{__install} -m 755 lib/libcudnn_adv_infer.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__install} -m 644 lib/libcudnn_adv_infer_static.a %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__install} -m 755 lib/libcudnn_adv_train.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__install} -m 644 lib/libcudnn_adv_train_static.a %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__install} -m 755 lib/libcudnn_cnn_infer.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__install} -m 644 lib/libcudnn_cnn_infer_static.a %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__install} -m 755 lib/libcudnn_cnn_train.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__install} -m 644 lib/libcudnn_cnn_train_static.a %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__install} -m 755 lib/libcudnn_ops_infer.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__install} -m 644 lib/libcudnn_ops_infer_static.a %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__install} -m 755 lib/libcudnn_ops_train.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__install} -m 644 lib/libcudnn_ops_train_static.a %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__install} -m 755 lib/libcudnn.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/
%{__ln_s} -f libcudnn_adv_infer.so.8 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_infer.so
%{__ln_s} -f libcudnn_adv_infer.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_infer.so.8
%{__ln_s} -f libcudnn_adv_infer_static.a %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_infer_static_v8.a
%{__ln_s} -f libcudnn_adv_train.so.8 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_train.so
%{__ln_s} -f libcudnn_adv_train.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_train.so.8
%{__ln_s} -f libcudnn_adv_train_static.a %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_train_static_v8.a
%{__ln_s} -f libcudnn_cnn_infer.so.8 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_infer.so
%{__ln_s} -f libcudnn_cnn_infer.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_infer.so.8
%{__ln_s} -f libcudnn_cnn_infer_static.a %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_infer_static_v8.a
%{__ln_s} -f libcudnn_cnn_train.so.8 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_train.so
%{__ln_s} -f libcudnn_cnn_train.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_train.so.8
%{__ln_s} -f libcudnn_cnn_train_static.a %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_train_static_v8.a
%{__ln_s} -f libcudnn_ops_infer.so.8 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_infer.so
%{__ln_s} -f libcudnn_ops_infer.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_infer.so.8
%{__ln_s} -f libcudnn_ops_infer_static.a %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_infer_static_v8.a
%{__ln_s} -f libcudnn_ops_train.so.8 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_train.so
%{__ln_s} -f libcudnn_ops_train.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_train.so.8
%{__ln_s} -f libcudnn_ops_train_static.a %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_train_static_v8.a
%{__ln_s} -f libcudnn.so.8 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn.so
%{__ln_s} -f libcudnn.so.8.4.0 %{buildroot}%{_prefix}/local/cuda-11.6/lib64/libcudnn.so.8
%{__install} -m 644 include/cudnn_adv_infer_v8.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_adv_train.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_v8.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_ops_train.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_cnn_train_v8.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_version_v8.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_ops_infer.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_cnn_infer_v8.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_ops_train_v8.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_adv_infer.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_backend_v8.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_adv_train_v8.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_cnn_train.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_backend.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_ops_infer_v8.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_version.h %{buildroot}%{_prefix}/local/cuda-11.6/include/
%{__install} -m 644 include/cudnn_cnn_infer.h %{buildroot}%{_prefix}/local/cuda-11.6/include/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}/local/cuda-11.6/cuDNN-LICENSE
%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_infer.so.8.4.0
%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_infer_static.a
%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_train.so.8.4.0
%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_train_static.a
%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_infer.so.8.4.0
%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_infer_static.a
%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_train.so.8.4.0
%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_train_static.a
%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_infer.so.8.4.0
%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_infer_static.a
%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_train.so.8.4.0
%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_train_static.a
%{_prefix}/local/cuda-11.6/lib64/libcudnn.so.8.4.0
%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_infer.so
%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_infer.so.8
%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_infer_static_v8.a
%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_train.so
%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_train.so.8
%{_prefix}/local/cuda-11.6/lib64/libcudnn_adv_train_static_v8.a
%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_infer.so
%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_infer.so.8
%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_infer_static_v8.a
%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_train.so
%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_train.so.8
%{_prefix}/local/cuda-11.6/lib64/libcudnn_cnn_train_static_v8.a
%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_infer.so
%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_infer.so.8
%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_infer_static_v8.a
%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_train.so
%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_train.so.8
%{_prefix}/local/cuda-11.6/lib64/libcudnn_ops_train_static_v8.a
%{_prefix}/local/cuda-11.6/lib64/libcudnn.so
%{_prefix}/local/cuda-11.6/lib64/libcudnn.so.8
%{_prefix}/local/cuda-11.6/include/cudnn_adv_infer.h
%{_prefix}/local/cuda-11.6/include/cudnn_adv_infer_v8.h
%{_prefix}/local/cuda-11.6/include/cudnn_adv_train.h
%{_prefix}/local/cuda-11.6/include/cudnn_adv_train_v8.h
%{_prefix}/local/cuda-11.6/include/cudnn_backend.h
%{_prefix}/local/cuda-11.6/include/cudnn_backend_v8.h
%{_prefix}/local/cuda-11.6/include/cudnn_cnn_infer.h
%{_prefix}/local/cuda-11.6/include/cudnn_cnn_infer_v8.h
%{_prefix}/local/cuda-11.6/include/cudnn_cnn_train.h
%{_prefix}/local/cuda-11.6/include/cudnn_cnn_train_v8.h
%{_prefix}/local/cuda-11.6/include/cudnn.h
%{_prefix}/local/cuda-11.6/include/cudnn_ops_infer.h
%{_prefix}/local/cuda-11.6/include/cudnn_ops_infer_v8.h
%{_prefix}/local/cuda-11.6/include/cudnn_ops_train.h
%{_prefix}/local/cuda-11.6/include/cudnn_ops_train_v8.h
%{_prefix}/local/cuda-11.6/include/cudnn_v8.h
%{_prefix}/local/cuda-11.6/include/cudnn_version.h
%{_prefix}/local/cuda-11.6/include/cudnn_version_v8.h

%changelog
* Wed Apr  6 2022 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 8.4.0.27
- Add "__os_install_post" global setting to prevent binary stripping so that
  binary files are packaged without modification and thus have the same checksum
  as those in the original tarball

* Tue Apr  5 2022 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 8.4.0.27
- Package libcudnn for Rocky Linux 8 and CUDA 11.6
