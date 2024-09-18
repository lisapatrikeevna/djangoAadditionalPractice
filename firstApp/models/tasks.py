from django.db import models


STATUS_CHOICES = [
    ('new', 'New'),
    ('in_progress', 'In progress'),
    ('pending', 'Pending'),
    ('blocked', 'Blocked'),
    ('done', 'Done'),
]


class CategoryT(models.Model):
    name = models.CharField('category name', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        unique_together = ('name',)



class Task(models.Model):
    title = models.CharField("unicum title for date", max_length=100, unique=True)
    description = models.TextField('description')
    # categories: Категории задачи. Многие ко многим.
    categories = models.ManyToManyField(CategoryT, related_name='tasks', blank=True)
    status = models.CharField('status', choices=STATUS_CHOICES, default='new',max_length=20)
    deadline = models.DateTimeField('deadline')
    created_at = models.DateTimeField('created at', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'
        verbose_name = 'Task'
        ordering = ['-created_at']
        unique_together = ('title',)


class SubTask(models.Model):
    title = models.CharField('subTitle', max_length=100)
    description = models.TextField('subDescription')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    status = models.CharField('status', choices=STATUS_CHOICES, default='new', max_length=20)
    deadline = models.DateTimeField('deadline')
    created_at = models.DateTimeField('created at', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at']
        verbose_name = 'SubTask'
        unique_together = ('title',)



