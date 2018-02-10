from django.http import JsonResponse


class FormMixin(object):
	def form_invalid():
			response = super(FormMixin, self).form_invalid(form)
			if self.request.is_ajax():
				return JsonResponse(form.errors, status = 400)
			else:
				return response

	def form_valid(self, form):
		response = super(FormMixin, self).form_valid(form)
		print('fomr is validate')
		# if self.request.is_ajax():
		# 	data = {
		# 	'message': 'add successfully'
		# 	}
		# 	return JsonResponse(data)
		# else:
		return response